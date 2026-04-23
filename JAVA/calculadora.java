public class calculadora {
    
    public int sumaInt(int a, int b) 
    {
            return a + b;
    }
    public int restaInt(int a, int b){return a - b;}
    public int multiplicacionInt(int a, int b){return a * b;}
    public int divisionInt(int a, int b){return a / b;}
    public float divisionfloat(int a, float b){return a / b;}
    public void main(String[] args) 
    {
        System.out.println("Saludo!");
        System.out.println(sumaInt(5, 3));
        System.out.println(restaInt(5, 3));
        System.out.println(multiplicacionInt(5, 3));
        System.out.println(divisionInt(6, 2));
        System.out.println(divisionfloat(6, 2.5f));
    }
    
}
