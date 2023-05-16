using ExemplosEstruturas.Models;

namespace ExemplosEstruturas.Services;

public class UsuarioService
{
    private SortedSet<Usuario> usuarios = new SortedSet<Usuario>();
    
    public void AdicionarUsuario()
    {
        Console.WriteLine("Digite o ID do novo Usuário");
        var id = Console.ReadLine();

        Console.WriteLine("Digite o Nome do novo Usuário");
        var nome = Console.ReadLine();

        var usuario = new Usuario()
        {
            Id = int.Parse(id ?? "0"),
            Nome = nome ?? string.Empty
        };

        if (usuarios.Add(usuario))
        {
            Console.WriteLine($"Usuário {usuario.Nome} com ID {usuario.Id} incluido com sucesso");
        }
        else
        {
            Console.WriteLine($"Usuário {usuario.Nome} com ID {usuario.Id} já existe no SET");
        }
    }

    public void ImprimirUsuarios()
    {
        foreach(var usuario in this.usuarios)
        {
            Console.WriteLine($"ID: {usuario.Id} | Nome: {usuario.Nome}");
        }
    }
}
