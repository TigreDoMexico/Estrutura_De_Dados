using ExemplosEstruturas.Models;
using ExemplosEstruturas.Repository;

namespace ExemplosEstruturas.Services;

public class CompraService
{
    private IRepository _repository;

    public CompraService(IRepository repository) => _repository = repository;

    public void AdicionarCompra()
    {
        Console.WriteLine("Digite o Valor da Compra");
        int valor = 0;
        int.TryParse(Console.ReadLine(), out valor);

        var compra = new Compra() { Valor = valor };

        Console.WriteLine("Digite o ID do Usuário ligado a Compra");
        this.ImprimirPossiveisUsuariosDaCompra();

        int idSelecionado = 0;
        int.TryParse(Console.ReadLine(), out idSelecionado);

        var usuario = _repository.ObterUsuarioPorId(idSelecionado);

        if(usuario is not null)
        {
            _repository.AdicionarCompra((usuario, compra));
            Console.WriteLine("Compra Criada com Sucesso!");
        }
        else
        {
            Console.WriteLine("Nenhum usuário selecionado! Compra cancelada!");
        }
    }

    public void ImprimirCompras()
    {
        foreach(var (usuario, compra) in _repository.ObterTodasCompras())
            Console.WriteLine($"Compra feita por {usuario.Nome} com valor R$ {compra.Valor}");
    }

    private void ImprimirPossiveisUsuariosDaCompra()
    {
        foreach(var usuario in _repository.ObterTodosUsuario())
            Console.WriteLine($"{usuario.Nome} -> ID: {usuario.Id}");
    }
}