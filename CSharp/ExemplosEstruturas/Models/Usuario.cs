namespace ExemplosEstruturas.Models;

public record Usuario : IComparable
{
    public int Id { get; set; }
    public string Nome { get; set; } = string.Empty;

    public int CompareTo(object? obj)
    {
        var user = (obj as Usuario);

        if(user is not null) {
            if(this.Id == user.Id) {
                return this.Nome.CompareTo(user.Nome);
            } 
            
            return this.Id.CompareTo(user.Id);
        }

        return -1;
    }
}
