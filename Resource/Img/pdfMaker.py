import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Datos de los 18 elementos narrativos con explicaciones detalladas y extendidas
elementos_narrativos = [
    # --- HISTORIA ---
    {
        "archivo": "Camino_del_Heroe", 
        "imagen": "ViajeDelHeroe", 
        "titulo": "El Camino del Héroe (Mitoestructura)", 
        "cat": "Historia", 
        "desc": "Un patrón clásico de 12 etapas basado en el monomito de Joseph Campbell que sigue el viaje, los desafíos y la transformación final de un protagonista. Su propósito fundamental es estructurar el crecimiento interno del personaje a la par de los peligros externos. Comienza en el mundo ordinario, pasa por la llamada a la aventura, cruza el umbral hacia lo desconocido, enfrenta pruebas y aliados, y culmina con el regreso a casa trayendo un elixir o aprendizaje que transforma su realidad."
    },
    {
        "archivo": "Estructura_Tres_Actos", 
        "imagen": "EstructuraDeTresActos", 
        "titulo": "Estructura de Tres Actos", 
        "cat": "Historia", 
        "desc": "La división tradicional y más efectiva del relato en tres partes clave: Planteamiento, Nudo y Desenlace. En el primer acto se establece el statu quo, se presentan los personajes principales y ocurre el incidente incitador que rompe la normalidad. El segundo acto, que ocupa la mayor parte de la obra, desarrolla el conflicto a través de obstáculos crecientes y giros dramáticos que llevan la tensión al límite. El tercer acto resuelve todas las líneas argumentales mediante un clímax de alta intensidad y establece un nuevo orden final."
    },
    {
        "archivo": "In_Media_Res", 
        "imagen": "InMediaRes", 
        "titulo": "In Media Res", 
        "cat": "Historia", 
        "desc": "Técnica narrativa de alto impacto donde la historia comienza directamente en mitad de la acción principal o en un momento crítico del conflicto, omitiendo las introducciones pasivas. Esto atrapa de inmediato la atención del espectador, sumergiéndolo en el suspenso o el peligro desde la primera página. Los antecedentes, las motivaciones de los personajes y los eventos previos necesarios para comprender el contexto general se van revelando de forma orgánica más adelante a través de diálogos, pistas o flashbacks."
    },
    {
        "archivo": "Arma_de_Chejov", 
        "imagen": "ArmaDeChejob", 
        "titulo": "El Arma de Chéjov", 
        "cat": "Historia", 
        "desc": "Principio dramático atribuido al escritor Antón Chéjov que dicta que cada elemento, detalle u objeto introducido en una historia debe ser estrictamente necesario y tener una función justificada en la trama. Si se menciona un rifle colgado en la pared en el primer acto, este debe dispararse de manera obligatoria en los actos siguientes. Su uso correcto evita la acumulación de detalles innecesarios, mantiene el foco de la narrativa y asegura que los eventos del clímax se sientan justificados y bien sembrados con anterioridad."
    },
    {
        "archivo": "Flashback_Analepsis", 
        "imagen": "Analepsis", 
        "titulo": "Flashback (Analepsis)", 
        "cat": "Historia", 
        "desc": "Una alteración deliberada de la cronología lineal que interrumpe la línea temporal presente para mostrar un evento crucial que ocurrió en el pasado. Se utiliza principalmente para proveer contexto emocional profundo, revelar secretos guardados por los personajes o justificar un comportamiento o trauma específico del protagonista en la actualidad. Para que sea efectivo, debe activarse mediante un detonante claro en el presente y aportar información estrictamente valiosa que cambie la percepción actual de la trama."
    },
    {
        "archivo": "Cliffhanger", 
        "imagen": "cliffhanger", 
        "titulo": "Cliffhanger", 
        "cat": "Historia", 
        "desc": "Un recurso estructural que consiste en terminar un capítulo, escena o acto de manera abrupta en el momento de máxima tensión, peligro o revelación impactante, dejando el destino de los personajes en el aire. Su objetivo principal es generar un suspenso irresistible que obligue al espectador a continuar consumiendo la obra de inmediato para descubrir la resolución. Es una herramienta fundamental en narrativas serializadas, pero requiere un equilibrio para no fatigar la confianza de la audiencia."
    },
    # --- PERSONAJES ---
    {
        "archivo": "Antiheroe", 
        "imagen": "Protagonista", 
        "titulo": "Protagonista Trágico / Antihéroe", 
        "cat": "Personajes", 
        "desc": "El personaje principal de la historia que conduce la trama pero carece de las virtudes moralistas, el idealismo o la nobleza tradicionales de un héroe clásico. Puede actuar por egoísmo, venganza o simple supervivencia, poseyendo fallas humanas profundas y métodos cuestionables. Sin embargo, su complejidad psicológica y sus dilemas internos suelen generar una fuerte empatía con la audiencia. Su arco suele explorar los matices grises de la moralidad y los sacrificios necesarios en mundos hostiles."
    },
    {
        "archivo": "El_Mentor", 
        "imagen": "Mentor", 
        "titulo": "El Mentor", 
        "cat": "Personajes", 
        "desc": "El arquetipo del maestro, guía o figura de sabiduría que entrena, aconseja y prepara al protagonista para enfrentar los desafíos de su viaje. Más allá de entregar conocimientos técnicos o artefactos mágicos, el mentor actúa como un pilar emocional y un catalizador para que el héroe descubra su verdadero potencial interno. Su partida o sacrificio suele ser un punto de inflexión crítico que obliga al protagonista a valerse por sí mismo y madurar de manera definitiva."
    },
    {
        "archivo": "Personaje_Espejo", 
        "imagen": "Espejo", 
        "titulo": "El Personaje Espejo (Foil)", 
        "cat": "Personajes", 
        "desc": "Un personaje diseñado específicamente para contrastar con otro (generalmente con el protagonista) con el fin de resaltar, profundizar y exponer de forma clara las virtudes, defectos, debilidades o filosofías de ambos. A través de sus diferencias en la toma de decisiones, trasfondo o actitudes, el personaje espejo expone ante la audiencia los rasgos que definen la identidad del héroe. No necesariamente debe ser un enemigo; a menudo es un aliado cercano con una perspectiva del mundo completamente opuesta."
    },
    {
        "archivo": "El_Antagonista", 
        "imagen": "Antagonista", 
        "titulo": "El Antagonista", 
        "cat": "Personajes", 
        "desc": "La fuerza principal que se opone de manera directa e implacable a las metas, valores y avance del protagonista. Puede manifestarse como un individuo con sus propias motivaciones complejas, un grupo organizado, una institución opresiva o incluso una fuerza abstracta de la naturaleza. Un gran antagonista no es malvado sin razón; tiene una filosofía interna sólida y representa el obstáculo definitivo que obliga al protagonista a transformarse y poner a prueba sus convicciones en el clímax."
    },
    {
        "archivo": "Personaje_Dinamico", 
        "imagen": "Dinamico", 
        "titulo": "Personaje Dinámico", 
        "cat": "Personajes", 
        "desc": "Cualquier individuo dentro de la obra que experimenta una transformación interna profunda, significativa y permanente en sus valores, creencias, personalidad o cosmovisión a raíz de los eventos de la trama. A diferencia de los personajes estáticos que permanecen iguales, el personaje dinámico es el núcleo del desarrollo dramático. Su evolución puede ser positiva (maduración, redención) o negativa (corrupción, caída en la locura), reflejando las consecuencias reales del conflicto en el alma humana."
    },
    {
        "archivo": "El_Heraldo", 
        "imagen": "Dinamico", 
        "titulo": "El Heraldo", 
        "cat": "Personajes", 
        "desc": "El arquetipo del mensajero, ya sea en forma de un personaje nuevo, una carta, un sueño o un evento catastrófico, cuya función primordial es irrumpir en la rutina del protagonista para plantearle un desafío insoslayable. El heraldo actúa como la fuerza inicial que desestabiliza el mundo ordinario y obliga al héroe a admitir la necesidad ineludible de un cambio absoluto. Su aparición es la que pone en marcha los engranajes del primer acto e inicia la verdadera aventura."
    },
    # --- OBJETOS ---
    {
        "archivo": "MacGuffin", 
        "imagen": "McGuffin", 
        "titulo": "MacGuffin", 
        "cat": "Objetos Narrativos", 
        "desc": "Un dispositivo, objeto o meta que sirve como el motor principal para hacer avanzar la trama y motivar las acciones de los personajes, pero que en realidad carece de relevancia intrínseca o explicación detallada por sí mismo. Su valor radica únicamente en lo mucho que los personajes lo desean, lo persiguen o intentan protegerlo. Es una herramienta ideal para iniciar conflictos dinámicos y persecuciones, permitiendo que el verdadero foco de la historia se concentre en las relaciones e interacciones humanas."
    },
    {
        "archivo": "Objeto_Simbolico", 
        "imagen": "totem", 
        "titulo": "Tótem / Objeto Simbólico", 
        "cat": "Objetos Narrativos", 
        "desc": "Un elemento físico tangible que condensa e irradia de manera puramente visual un concepto abstracto, una emoción profunda, un pacto inquebrantable o la identidad oculta de un personaje. A lo largo del relato, el estado físico de este objeto (si se rompe, se ensucia, se repara o se pierde) suele reflejar de manera paralela la situación interna o el declive emocional del personaje asociado, sirviendo como una poderosa herramienta de metáfora visual continua."
    },
    {
        "archivo": "Objeto_Magico", 
        "imagen": "ObjetoMagico", 
        "titulo": "El Objeto Mágico / Catalizador",
        "cat": "Objetos Narrativos",
        "desc": "Un artefacto, reliquia o dispositivo tecnológico avanzado que posee propiedades extraordinarias bien definidas y cuya aparición altera por completo el balance de poder en la historia. Funciona como un catalizador del conflicto: otorga capacidades únicas al portador pero, al mismo tiempo, acarrea grandes responsabilidades, peligros implícitos o atrae la codicia de fuerzas oscuras. Su uso suele estar condicionado a reglas estrictas que desafían el ingenio del protagonista."
    },
    {
        "archivo": "Pista_Falsa",
        "imagen": "PistaFalsa",
        "titulo": "La Pista Falsa (Red Herring)",
        "cat": "Objetos Narrativos",
        "desc": "Un indicio, objeto o fragmento de información colocado de manera sumamente deliberada por el autor para desviar la atención de los investigadores, los personajes o la propia audiencia hacia una conclusión errónea. Es un elemento fundamental en las historias de misterio, suspenso y thrillers psicológicos. Su propósito técnico es enriquecer el conflicto, construir giros dramáticos inesperados y poner a prueba el razonamiento analítico de los personajes antes de revelar la verdad oculta."
    },
    {
        "archivo": "Recurso_Epistolar",
        "imagen": "Epistolar",
        "titulo": "El Diario o Carta (Recurso Epistolar)",
        "cat": "Objetos Narrativos",
        "desc": "Un documento escrito real e íntimo dentro del mundo de la historia que funciona como una ventana directa a los pensamientos sin filtro, secretos del pasado o confesiones de un personaje. Permite revelar antecedentes indispensables de la trama y giros argumentales de forma orgánica, eliminando la necesidad de emplear un narrador omnisciente artificial. Aporta verosimilitud y sumerge al lector en una atmósfera de complicidad absoluta con los textos descubiertos."
    },
    {
        "archivo": "Reliquia_Legado",
        "imagen": "RecursoLegado",
        "titulo": "Reliquia / Objeto de Legado",
        "cat": "Objetos Narrativos",
        "desc": "Un objeto con un inmenso valor histórico o familiar que conecta de forma ineludible al protagonista con sus ancestros, una profecía antigua o una herencia olvidada de su linaje. Funciona como un recordatorio físico constante de sus deberes morales, de su destino o de los errores del pasado que está obligado a enmendar. Su posesión suele otorgar legitimidad ante los demás personajes y marca el inicio de la aceptación de su verdadera identidad."
    }
]


def buscar_imagen_local(nombre_base):
    extensiones = ['.png', '.jpg', '.jpeg','.webp',".avif"]
    for ext in extensiones:
        ruta_completa = f"{nombre_base}{ext}"
        if os.path.exists(ruta_completa):
            return ruta_completa
    return None


def generar_pdfs():
    styles = getSampleStyleSheet()
    
    # Estilos limpios adaptados para manejar bloques de texto más densos
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#1A1A1A'),
        spaceAfter=4
    )
    cat_style = ParagraphStyle(
        'DocCat',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#666666'),
        spaceAfter=16
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=18,
        textColor=colors.HexColor('#222222'),
        alignment=4  # Justificado para textos más largos
    )

    for el in elementos_narrativos:
        nombre_pdf = f"{el['archivo']}.pdf"
        doc = SimpleDocTemplate(
            nombre_pdf, 
            pagesize=letter, 
            leftMargin=45, 
            rightMargin=45, 
            topMargin=45, 
            bottomMargin=45
        )
        story = []

        # 1. Título y Categoría
        story.append(Paragraph(el['titulo'], title_style))
        story.append(Paragraph(f"Categoría: {el['cat']}", cat_style))

        # 2. Imagen Local
        ruta_img = buscar_imagen_local(el['imagen'])
        if ruta_img:
            story.append(Image(ruta_img, width=420, height=230))
        else:
            print(f"Aviso: No se encontró la imagen '{el['imagen']}' para el archivo {nombre_pdf}.")
        
        story.append(Spacer(1, 20))

        # 3. Explicación Narrativa Detallada
        story.append(Paragraph(el['desc'], body_style))

        # Compilación del archivo
        doc.build(story)
        print(f"PDF generado exitosamente: {nombre_pdf}")


if __name__ == "__main__":
    generar_pdfs()