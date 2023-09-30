try:
    fulano.__salary = (8000000) #não posso deixar o salario publico, porque se não
    #qualquer um poderia alterar esses dados. Para evitar esse uso, colocamos
    # __ (duas vezes underline) para tornar esse atributo privado
except:
    print("Não foi possivel usar o codigo acima")