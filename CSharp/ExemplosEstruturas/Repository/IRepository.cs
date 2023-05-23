using ExemplosEstruturas.Models;

namespace ExemplosEstruturas.Repository;

public interface IRepository
{
    public bool AdicionarUsuario(Usuario usuario);
    public bool AdicionarCompra((Usuario, Compra) compra);
    public Usuario? ObterUsuarioPorId(int id);
    public List<Usuario> ObterTodosUsuario();
    public List<(Usuario, Compra)> ObterTodasCompras();
}
