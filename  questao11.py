import matplotlib.pyplot as plt

def plot_complex_multiplication(c):
    # Componentes real e imaginário do número complexo
    real_part = c.real
    imag_part = c.imag
    
    # Multiplicação pelo componente real
    result_real = c * real_part
    
    # Multiplicação pelo componente imaginário
    result_imag = c * imag_part
    
    # Configuração do gráfico
    plt.figure(figsize=(10, 5))
    
    # Plotagem dos vetores
    plt.quiver(0, 0, real_part, imag_part, angles='xy', scale_units='xy', scale=1, color='r', label='Número Complexo')
    plt.quiver(0, 0, result_real.real, result_real.imag, angles='xy', scale_units='xy', scale=1, color='g', label='c x r')
    plt.quiver(0, 0, result_imag.real, result_imag.imag, angles='xy', scale_units='xy', scale=1, color='b', label='c x i')
    
    # Configurações adicionais do gráfico
    plt.xlim(min(real_part, result_real.real, result_imag.real) - 1, max(real_part, result_real.real, result_imag.real) + 1)
    plt.ylim(min(imag_part, result_real.imag, result_imag.imag) - 1, max(imag_part, result_real.imag, result_imag.imag) + 1)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.title('Multiplicação de um Número Complexo pelo seu Componente Real e Imaginário')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.show()

# Teste da função com um número complexo
c = 2 + 3j
plot_complex_multiplication(c)