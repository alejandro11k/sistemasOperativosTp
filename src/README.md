Pendientes del TP

Shell
Disco
Programa
Cola de ready, waiting
Schedule 
- Falta que el pcb saque de la cola de  ready y se lo de a la cpu

"un test que deberían hacer:
agarrá un programa, una instrucción de I/O 
dáselo al cpu
cpu.run
y hacés un assert que levante la interrupción de I/O en la cola de interrupciones" (esto lo dijo el ayudante y lo copié como pude.

Correcciones del profe cuando vino a ver nuestro TP

clase.variable para interrupciones
NO USAR STRINGS
ponerlo en irq (más fácil para cambiar)

interruption_manager -> está vacío al crearlo
no tengo valor x defecto para el / kill ni para ninguna interrupción
lo definís en el test
o sumás un método para agregarlo (add del diccionario)

