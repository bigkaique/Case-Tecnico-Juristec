
# criando uma classe para representar uma televisao com atributos de canal e volume, e metodos para mudar o canal e ajustar o volume.
class MyTelevisao:
    def __init__(sel):
        sel.canal = 1  # canal inicial
        sel.volume = 50  # volume inicial
        sel.mudo = False  # estado inicial do mudo

    # colocando atributo para mudar o canal
    def mudar_canal(sel, canal):
        if 1 <= canal <= 100:
            sel.canal = canal

    # um metodo para aumentar o volume que serve para aumentar o volume da televisao, garantindo que o volume nao fique acima de 100.
    def aumentar_volume(sel):
        if sel.volume < 100:
            sel.volume += 1

    # um metodo para diminuir o volume que serve para diminuir o volume da televisao, garantindo que o volume nao fique abaixo de 0.
    def diminuir_volume(sel):
        if sel.volume > 0:
            sel.volume -= 1

    # um metodo para deixar a televisao mudo caso ele deseje nao ter mais barulho ou esconde algo, que define o volume como 0.
    def deixa_mudo(sel):
        sel.mudo = True
        sel.volume = 0



                                 # --- ÁREA DE TESTES ---


input("Pressione Enter para iniciar os testes...")
canal_desejado = int(input("digite o canal desejado: de 1 a 100: "))
while canal_desejado < 1 or canal_desejado > 100:
    canal_desejado = int(input("canal inválido. digite um valor entre 1 e 100: "))
minha_tv = MyTelevisao()
minha_tv.mudar_canal(canal_desejado)


volume_desejado = int(input("qual o volume que voce deseja? de 0 a 100: "))
while volume_desejado < 0 or volume_desejado > 100:
    volume_desejado = int(input("volume inválido "))
minha_tv.aumentar_volume() 
while minha_tv.volume < volume_desejado:
    minha_tv.aumentar_volume() # para aumentar o volume da TV ate atingir o volume desejado.
while minha_tv.volume > volume_desejado:
    minha_tv.diminuir_volume() # para diminuir o volume da TV ate atingir o volume desejado.

print(f"Canal atual: {minha_tv.canal}")
print(f"Volume atual: {minha_tv.volume}")

# solicitando ao usuário que insira se deseja deixar a TV no modo mudo
mudo_input = input("Deseja deixar a TV no modo mudo? (s/n): ").strip().lower()
if mudo_input == 's':
    minha_tv.deixa_mudo()
    print("A TV está agora no modo mudo.")
else:
    print("A TV não está no modo mudo.")


