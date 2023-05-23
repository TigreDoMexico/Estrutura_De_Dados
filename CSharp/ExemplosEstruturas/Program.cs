using ExemplosEstruturas.Services;
using ExemplosEstruturas.Repository;

var repository = new Repository();

var usuarioService = new UsuarioService(repository);

for(int i = 0; i < 2; i++)
{
    usuarioService.AdicionarUsuario();
}

usuarioService.ImprimirUsuarios();

var compraService = new CompraService(repository);

for(int i = 0; i < 3; i++)
{
    compraService.AdicionarCompra();
}

compraService.ImprimirCompras();