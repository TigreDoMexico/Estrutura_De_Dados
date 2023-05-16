using ExemplosEstruturas.Services;

var usuarioService = new UsuarioService();

for(int i = 0; i < 5; i++)
{
    usuarioService.AdicionarUsuario();
}

usuarioService.ImprimirUsuarios();