using System.Linq;
using ExemplosEstruturas.Models;

namespace ExemplosEstruturas.Repository;

public class Repository : IRepository
{
    private SortedSet<Usuario> usuarios = new SortedSet<Usuario>();
    private List<Tuple<Usuario, Compra>> compras = new();

    public bool AdicionarCompra((Usuario, Compra) compra)
    {
        try
        {
            compras.Add(compra.ToTuple<Usuario, Compra>());
            return true;
        }
        catch (Exception)
        {
            return false;
        }
    }

    public List<(Usuario, Compra)> ObterTodasCompras() => this.compras.Select(c => c.ToValueTuple()).ToList();
    
    public bool AdicionarUsuario(Usuario usuario) => usuarios.Add(usuario);

    public List<Usuario> ObterTodosUsuario() => usuarios.ToList();

    public Usuario? ObterUsuarioPorId(int id) => usuarios.FirstOrDefault(a => a.Id == id);
}
