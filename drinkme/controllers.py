import selector
from pprint import pformat
import Image, cStringIO
import cgi

def square_resize(img,size):
    sizes = list(img.size)
    trim = abs(sizes[1] - sizes[0]) / 2
    if sizes[0] < sizes[1]:
        img = img.crop((0,trim,sizes[0],trim + sizes[0]))
    if sizes[1] < sizes[0]:
        img = img.crop((trim,0,trim + sizes[1],sizes[1]))
    return img.resize((size,size),Image.ANTIALIAS)    

def resize(img,size=100,square=False):
    if square:
        img = square_resize(img,size)
    else:
        img.thumbnail((size,size),Image.ANTIALIAS)

    # workaround for PIL bug
    if img.size[0] == 0:
        img = img.resize((1,img.size[1]))
    if img.size[1] == 0:
        img = img.resize((img.size[0],1))
        
    return img

mapping = {'image/jpeg' : 'JPEG',
           'image/gif' : 'GIF',
           'image/png' : 'PNG'}

def get_format_from_content_type(ct):
    return mapping.get(ct,'JPEG')

class InputProcessed(object):
    def read(self, *args):
        raise EOFError(
            'The wsgi.input stream has already been consumed')
    readline = readlines = __iter__ = read

def cgi_get(fs,key,default):
    """ cgi fieldstorage is broken. it pretends to be a dict but doesn't implement
    a get() method. and the thing it returns isn't really a value. :( """
    try:
        return fs[key].file.read()
    except:
        return default


class Root:
    def get_post_form(self,environ):
        input = environ['wsgi.input']
        post_form = environ.get('wsgi.post_form')
        if (post_form is not None and post_form[0] is input):
            return post_form[2]
        fs = cgi.FieldStorage(fp=input,
                              environ=environ,
                              keep_blank_values=1)
        new_input = InputProcessed()
        post_form = (new_input, input, fs)
        environ['wsgi.post_form'] = post_form
        environ['wsgi.input'] = new_input
        return fs

    
    def __call__(self, environ, start_response):
        post_data = self.get_post_form(environ)
        size = 100
        image = post_data['image']
        size = cgi_get(post_data,'size',100)
        square = cgi_get(post_data,'square',0) != 0
        filename = image.filename
        im = Image.open(image.file)
        im = resize(im,int(size),square)
        
        content_type = image.headers.get('Content-Type','image/jpeg')
        if content_type not in mapping.keys():
            yield "unsupported image type"
        start_response("200 OK", [('Content-Type',content_type)])
        output = cStringIO.StringIO()
        im.save(output,get_format_from_content_type(content_type))
        yield output.getvalue()
        
urls = selector.Selector()
urls.add('/[{action}]', _ANY_=Root())


