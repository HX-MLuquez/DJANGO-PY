def sigue_o_no():
    otro_calculo = input("Desea realizar otro cálculo: [s/n]")
    if  otro_calculo == "n":
        return False
    elif otro_calculo == "s":
        return True 
    else:
        exit()
        # return False

    
if __name__ == "__main__":
    print(sigue_o_no())