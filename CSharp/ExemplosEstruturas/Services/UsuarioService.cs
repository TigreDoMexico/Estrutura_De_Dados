using ExemplosEstruturas.Models;
using ExemplosEstruturas.Repository;

namespace ExemplosEstruturas.Services;

public class UsuarioService
{
    private IRepository _repository;

    public UsuarioService(IRepository repository) => _repository = repository;

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

        if (_repository.AdicionarUsuario(usuario))
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
        foreach(var usuario in _repository.ObterTodosUsuario())
        {
            Console.WriteLine($"ID: {usuario.Id} | Nome: {usuario.Nome}");
        }
    }
}
