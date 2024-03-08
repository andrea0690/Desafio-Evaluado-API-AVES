from string import Template

def get_img_template():
    return Template("""
        <div class="card m-2" style="width: 18rem;">
            <img src="$url" class="card-img-top" alt="$id">
            <div class="card-body">
                <p class="card-text"><b>Nombre</b>: $name</p>
                <p class="card-text"><b>Name</b>: $name2</p>
            </div>
        </div>
    """
)
    
def get_esqueleto():
    return Template('''
            <!DOCTYPE html>
                <html>
                <head>
                    <title>AVES DE CHILE</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
                </head>
                <body>
                    <div class="container">
                        <div class="row">
                            <h1 class="text-center">AVES</h1>

                            $body
                        </div>
                    </div>


                </body>
                </html>
        ''')

# imagen = img_template.substitute(url = 'Hola')