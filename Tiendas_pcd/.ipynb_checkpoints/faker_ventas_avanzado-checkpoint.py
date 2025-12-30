from faker import Faker
import random
import csv
from datetime import datetime, timedelta

fake = Faker("es_MX")

# ============================================================================
# CATÁLOGO DE PRODUCTOS (100 productos con ID)
# ============================================================================
PRODUCTOS = {
    1: "Coca-Cola 600ml", 2: "Pepsi 600ml", 3: "Agua Bonafont 1L", 
    4: "Galletas María Gamesa", 5: "Pan Bimbo Blanco", 6: "Leche Lala Entera 1L",
    7: "Café Soluble Nescafé", 8: "Arroz Verde Valle", 9: "Frijoles Isadora",
    10: "Aceite Nutrioli 1L", 11: "Atún Herdez en Agua", 12: "Yogurt Danone",
    13: "Cereal Zucaritas", 14: "Jugo Jumex Durazno", 15: "Huevo San Juan 18p",
    16: "Tortillas de Maíz Maseca", 17: "Queso Oaxaca Lala", 18: "Jugo del Valle Mango",
    19: "Refresco Fanta 600ml", 20: "Gatorade Azul 500ml", 21: "Sabritas Clásicas",
    22: "Doritos Nacho", 23: "Chocolate Abuelita Tabletas", 24: "Pan Tostado Bimbo",
    25: "Jamón de Pavo FUD", 26: "Crema Alpura", 27: "Mantequilla Gloria",
    28: "Azúcar Zulka 1kg", 29: "Sal La Fina", 30: "Pasta La Moderna",
    31: "Sopa Maruchan Pollo", 32: "Agua Epura 1L", 33: "Red Bull",
    34: "Monster Energy", 35: "Café de Olla La Finca", 36: "Aceite Capullo",
    37: "Mayonesa McCormick", 38: "Ketchup Heinz", 39: "Mostaza French's",
    40: "Queso Panela Lala", 41: "Chobani Yogurt", 42: "Yoghurt Griego Yoplait",
    43: "Galletas Oreo", 44: "Cacahuates Kacang", 45: "Mix de Nueces Member's Mark",
    46: "Chocolate Snickers", 47: "Chocolate Milky Way", 48: "Refresco Sprite 600ml",
    49: "Powerade Moras 500ml", 50: "Pan Molido Bimbo", 51: "Té Limón Lipton",
    52: "Avena Quaker", 53: "Cacahuates Hot Nuts", 54: "Agua Mineral Topo Chico",
    55: "Vino Tinto Casillero del Diablo", 56: "Cerveza Corona 355ml",
    57: "Cerveza Modelo Especial", 58: "Cerveza Victoria", 59: "Ron Bacardí Blanco",
    60: "Tequila José Cuervo Tradicional", 61: "Mezcal 400 Conejos",
    62: "Salsa Valentina", 63: "Salsa Bufalo", 64: "Café Garat",
    65: "Leche Deslactosada Lala", 66: "Yogurt Activia", 67: "Gansito Marinela",
    68: "Pingüinos Marinela", 69: "Chocolate Carlos V", 70: "Pan Integral Bimbo",
    71: "Barra de Granola Nature Valley", 72: "Suero Electrolit",
    73: "Suero Pedialyte", 74: "Papas Ruffles Queso", 75: "Churrumais",
    76: "Cereal Cheerios", 77: "Cereal Choco Krispis", 78: "Cereal Froot Loops",
    79: "Jugo Boing Mango", 80: "Jugo Boing Guayaba", 81: "Refresco Manzanita Sol",
    82: "Choco Milk", 83: "Nescafé Cappuccino", 84: "Té Chai Twinings",
    85: "Cerveza Heineken", 86: "Cerveza Stella Artois", 87: "Agua Ciel 1L",
    88: "Refresco Fresca 600ml", 89: "Mole Doña María", 90: "Tortillas Tía Rosa",
    91: "Atún Dolores", 92: "Sardinas La Sirena", 93: "Sopa Campbell's",
    94: "Frijoles Bayos La Sierra", 95: "Helado Holanda",
    96: "Queso Manchego NocheBuena", 97: "Crema Philadelphia", 98: "Pan de Caja Wonder",
    99: "Papel Higiénico Pétalo", 100: "Detergente Ariel 1kg"
}

# ============================================================================
# CATÁLOGO DE TIENDAS (ID con nombre y categoría)
# ============================================================================
TIENDAS = {
    1: {"nombre": "Walmart", "categoria": "Autoservicio"},
    2: {"nombre": "Sam's Club", "categoria": "Mayoreo"},
    3: {"nombre": "Bodega Aurrera", "categoria": "Descuento"},
    4: {"nombre": "Soriana", "categoria": "Autoservicio"},
    5: {"nombre": "Chedraui", "categoria": "Autoservicio"},
    6: {"nombre": "City Market", "categoria": "Premium"},
    7: {"nombre": "La Comer", "categoria": "Premium"},
    8: {"nombre": "Costco", "categoria": "Mayoreo"},
    9: {"nombre": "Tienda 3B", "categoria": "Descuento"},
    10: {"nombre": "Oxxo", "categoria": "Conveniencia"}
}

# ============================================================================
# CIUDADES
# ============================================================================
CIUDADES = ["CDMX", "GDL", "MTY", "PUEBLA", "CANCUN"]

# Variantes con errores de ciudades
CIUDADES_ERRORES = {
    "CDMX": ["cdmx", "Cdmx", "CD MX", "Ciudad de Mexico", "DF", "CIUDAD MEXICO"],
    "GDL": ["gdl", "Gdl", "GUADALAJARA", "Guadalajara", "GDL ", " GDL"],
    "MTY": ["mty", "Mty", "MONTERREY", "Monterrey", "MTY ", "Mty."],
    "PUEBLA": ["puebla", "Puebla", "PUEBLA ", "Pue", "PUE"],
    "CANCUN": ["cancun", "Cancun", "Cancún", "CANCÚN", "QRoo", "Q.Roo"]
}

# ============================================================================
# RANGOS DE PRECIOS POR PRODUCTO (Precios base en MXN)
# ============================================================================
PRECIOS_BASE = {
    1: (15, 18), 2: (14, 17), 3: (8, 12), 4: (20, 25), 5: (35, 42),
    6: (22, 28), 7: (85, 110), 8: (25, 35), 9: (18, 24), 10: (45, 55),
    11: (28, 35), 12: (15, 20), 13: (45, 60), 14: (12, 16), 15: (55, 70),
    16: (18, 25), 17: (65, 85), 18: (15, 20), 19: (15, 18), 20: (18, 22),
    21: (18, 22), 22: (20, 25), 23: (32, 40), 24: (28, 35), 25: (65, 80),
    26: (35, 45), 27: (45, 60), 28: (30, 38), 29: (8, 12), 30: (18, 24),
    31: (14, 18), 32: (9, 13), 33: (35, 42), 34: (38, 45), 35: (55, 70),
    36: (42, 52), 37: (48, 58), 38: (35, 45), 39: (30, 38), 40: (55, 70),
    41: (25, 32), 42: (28, 35), 43: (28, 35), 44: (22, 28), 45: (85, 110),
    46: (15, 20), 47: (15, 20), 48: (15, 18), 49: (18, 22), 50: (25, 32),
    51: (35, 45), 52: (42, 55), 53: (25, 32), 54: (15, 20), 55: (180, 250),
    56: (18, 22), 57: (17, 21), 58: (16, 20), 59: (220, 280), 60: (280, 350),
    61: (350, 450), 62: (18, 24), 63: (20, 26), 64: (95, 120), 65: (24, 30),
    66: (18, 24), 67: (13, 17), 68: (14, 18), 69: (12, 16), 70: (38, 48),
    71: (28, 35), 72: (22, 28), 73: (85, 110), 74: (20, 25), 75: (16, 20),
    76: (48, 62), 77: (45, 58), 78: (46, 60), 79: (12, 16), 80: (12, 16),
    81: (15, 18), 82: (16, 20), 83: (45, 58), 84: (65, 85), 85: (22, 28),
    86: (28, 35), 87: (9, 13), 88: (15, 18), 89: (35, 45), 90: (20, 26),
    91: (26, 32), 92: (24, 30), 93: (32, 42), 94: (20, 26), 95: (65, 85),
    96: (85, 110), 97: (55, 70), 98: (32, 42), 99: (95, 120), 100: (145, 180)
}

# ============================================================================
# FUNCIONES DE GENERACIÓN DE ERRORES
# ============================================================================

def error_ortografico_simple(texto: str) -> str:
    """Introduce un error simple: borrar o cambiar un carácter."""
    if not texto or len(texto) < 2:
        return texto
    texto = list(texto)
    idx = random.randint(0, len(texto) - 1)
    accion = random.choice(["borrar", "reemplazar", "duplicar"])
    
    if accion == "borrar":
        del texto[idx]
    elif accion == "reemplazar":
        texto[idx] = random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    else:  # duplicar
        texto.insert(idx, texto[idx])
    
    return "".join(texto)

def generar_fecha_aleatoria(fecha_inicio, fecha_fin):
    """Genera una fecha aleatoria entre dos fechas."""
    delta = fecha_fin - fecha_inicio
    dias_random = random.randint(0, delta.days)
    return fecha_inicio + timedelta(days=dias_random)

def aplicar_ruido_ciudad(ciudad):
    """Aplica errores a la ciudad."""
    tipo = random.choice(["error_tipico", "espacios", "minusculas", "typo"])
    
    if tipo == "error_tipico":
        return random.choice(CIUDADES_ERRORES[ciudad])
    elif tipo == "espacios":
        return f"  {ciudad}  "
    elif tipo == "minusculas":
        return ciudad.lower()
    else:
        return error_ortografico_simple(ciudad)

def aplicar_ruido_precio(precio):
    """Aplica errores al formato del precio."""
    tipo = random.choice(["coma", "texto", "espacios", "simbolo"])
    
    if tipo == "coma":
        return str(precio).replace(".", ",")
    elif tipo == "texto":
        return f"{precio} pesos"
    elif tipo == "espacios":
        return f"  {precio}  "
    else:
        return f"${precio}"

def aplicar_ruido_fecha(fecha):
    """Aplica errores al formato de la fecha."""
    tipo = random.choice(["formato_us", "sin_ceros", "espacios", "barras"])
    fecha_str = fecha.strftime("%Y-%m-%d")
    
    if tipo == "formato_us":
        return fecha.strftime("%m/%d/%Y")
    elif tipo == "sin_ceros":
        # Windows-compatible: remover ceros manualmente en lugar de usar %-m
        mes = str(fecha.month)
        dia = str(fecha.day)
        return f"{fecha.year}-{mes}-{dia}" if random.random() < 0.5 else fecha_str
    elif tipo == "espacios":
        return f" {fecha_str} "
    else:
        return fecha.strftime("%d/%m/%Y")

def aplicar_ruido_id(id_valor):
    """Aplica errores al ID."""
    tipo = random.choice(["espacios", "texto", "ceros"])
    
    if tipo == "espacios":
        return f" {id_valor} "
    elif tipo == "texto":
        return f"ID{id_valor}"
    else:
        return f"{id_valor:04d}"  # Con ceros a la izquierda

# ============================================================================
# FUNCIÓN PRINCIPAL DE GENERACIÓN
# ============================================================================

def generar_dataset_ventas(
    num_registros: int = 1000000,
    porcentaje_campos_vacios: float = 5,
    porcentaje_ruido: float = 10,
    porcentaje_id_mal_asociado: float = 3,
    porcentaje_duplicados: float = 3,
    nombre_archivo: str = "ventas_retail_mexico.csv",
    fecha_inicio: str = "2023-01-01",
    fecha_fin: str = "2024-12-31"
):
    """
    Genera un dataset de ventas con datos sucios.
    
    Args:
        num_registros: Número de registros a generar
        porcentaje_campos_vacios: % de registros con campos vacíos
        porcentaje_ruido: % de registros con errores de formato
        porcentaje_id_mal_asociado: % de registros con ID producto mal asociado
        porcentaje_duplicados: % de registros duplicados a generar
        nombre_archivo: Nombre del archivo CSV de salida
        fecha_inicio: Fecha de inicio del período (YYYY-MM-DD)
        fecha_fin: Fecha de fin del período (YYYY-MM-DD)
    """
    
    # Validaciones de parámetros
    if num_registros <= 0:
        raise ValueError("num_registros debe ser mayor a 0")
    if not (0 <= porcentaje_campos_vacios <= 100):
        raise ValueError("porcentaje_campos_vacios debe estar entre 0 y 100")
    if not (0 <= porcentaje_ruido <= 100):
        raise ValueError("porcentaje_ruido debe estar entre 0 y 100")
    if not (0 <= porcentaje_id_mal_asociado <= 100):
        raise ValueError("porcentaje_id_mal_asociado debe estar entre 0 y 100")
    if not (0 <= porcentaje_duplicados <= 100):
        raise ValueError("porcentaje_duplicados debe estar entre 0 y 100")
    
    print(f"\n{'='*70}")
    print(f"GENERADOR DE DATOS DE VENTAS - RETAIL MÉXICO")
    print(f"{'='*70}\n")
    print(f"Generando {num_registros:,} registros base...")
    
    # Convertir fechas con manejo de errores
    try:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
        if fecha_inicio_dt > fecha_fin_dt:
            raise ValueError("fecha_inicio debe ser anterior a fecha_fin")
    except ValueError as e:
        print(f"❌ Error en el formato de fechas: {e}")
        print("   Formato esperado: YYYY-MM-DD (ej: 2025-01-01)")
        raise
    
    filas = []
    
    # Generar registros limpios
    for i in range(1, num_registros + 1):
        id_transaccion = i
        id_producto = random.randint(1, 100)
        nombre_producto = PRODUCTOS[id_producto]
        precio_min, precio_max = PRECIOS_BASE[id_producto]
        precio = round(random.uniform(precio_min, precio_max), 2)
        id_tienda = random.randint(1, 10)
        nombre_tienda = TIENDAS[id_tienda]["nombre"]
        categoria_tienda = TIENDAS[id_tienda]["categoria"]
        ciudad = random.choice(CIUDADES)
        fecha = generar_fecha_aleatoria(fecha_inicio_dt, fecha_fin_dt)
        fecha_str = fecha.strftime("%Y-%m-%d")
        
        fila = [
            id_transaccion, id_producto, nombre_producto, precio,
            id_tienda, nombre_tienda, categoria_tienda, ciudad, fecha_str
        ]
        filas.append(fila)
        
        if i % 100000 == 0:
            print(f"  Progreso: {i:,}/{num_registros:,} registros generados...")
    
    print(f"\nGeneración base completada: {num_registros:,} registros\n")
    
    indices = list(range(num_registros))
    
    # ========================================================================
    # APLICAR DUPLICADOS
    # ========================================================================
    num_duplicados = int(num_registros * porcentaje_duplicados / 100)
    registros_duplicados = 0
    
    if num_duplicados > 0:
        print(f"Aplicando {num_duplicados:,} registros duplicados...")
        
        # 60% duplicados exactos, 40% duplicados parciales
        num_exactos = int(num_duplicados * 0.6)
        num_parciales = num_duplicados - num_exactos
        
        # DUPLICADOS EXACTOS
        if num_exactos > 0:
            indices_a_duplicar = random.sample(indices, num_exactos)
            for idx in indices_a_duplicar:
                # Copiar el registro exactamente
                fila_duplicada = filas[idx].copy()
                # Cambiar el ID de transacción para que sea único
                fila_duplicada[0] = len(filas) + 1
                filas.append(fila_duplicada)
                registros_duplicados += 1
        
        # DUPLICADOS PARCIALES (con pequeñas variaciones)
        if num_parciales > 0:
            indices_a_duplicar = random.sample(indices, num_parciales)
            for idx in indices_a_duplicar:
                fila_duplicada = filas[idx].copy()
                fila_duplicada[0] = len(filas) + 1  # Nuevo ID
                
                # Aplicar pequeña variación
                tipo_variacion = random.choice([
                    "precio_similar", "formato_nombre", "formato_ciudad", "formato_fecha"
                ])
                
                if tipo_variacion == "precio_similar" and fila_duplicada[3]:
                    # Variar precio en ±0.01 a ±2.00
                    try:
                        precio_original = float(str(fila_duplicada[3]).replace(",", ".").replace(" pesos", "").replace(" MXN", "").replace("$", "").strip())
                        variacion = round(random.uniform(-2, 2), 2)
                        nuevo_precio = round(precio_original + variacion, 2)
                        # Asegurar que el precio no sea negativo
                        fila_duplicada[3] = max(0.01, nuevo_precio)
                    except (ValueError, TypeError) as e:
                        # Mantener el precio original si hay error
                        pass
                
                elif tipo_variacion == "formato_nombre" and fila_duplicada[2]:
                    # Cambiar formato del nombre (mayúsculas/minúsculas/espacios)
                    opciones = ["upper", "lower", "title", "spaces"]
                    formato = random.choice(opciones)
                    if formato == "upper":
                        fila_duplicada[2] = fila_duplicada[2].upper()
                    elif formato == "lower":
                        fila_duplicada[2] = fila_duplicada[2].lower()
                    elif formato == "title":
                        fila_duplicada[2] = fila_duplicada[2].title()
                    else:
                        fila_duplicada[2] = f" {fila_duplicada[2]} "
                
                elif tipo_variacion == "formato_ciudad" and fila_duplicada[7]:
                    # Cambiar formato de ciudad
                    ciudad_original = fila_duplicada[7].strip()
                    if ciudad_original in CIUDADES:
                        fila_duplicada[7] = aplicar_ruido_ciudad(ciudad_original)
                
                elif tipo_variacion == "formato_fecha" and fila_duplicada[8]:
                    # Cambiar formato de fecha
                    try:
                        # Intentar varios formatos de fecha
                        fecha_str = str(fila_duplicada[8]).strip()
                        for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]:
                            try:
                                fecha_obj = datetime.strptime(fecha_str, fmt)
                                fila_duplicada[8] = aplicar_ruido_fecha(fecha_obj)
                                break
                            except ValueError:
                                continue
                    except Exception as e:
                        # Mantener la fecha original si hay error
                        pass
                
                filas.append(fila_duplicada)
                registros_duplicados += 1
        
        # Actualizar índices con los nuevos registros
        indices = list(range(len(filas)))
        print(f"  - Duplicados exactos: {num_exactos:,}")
        print(f"  - Duplicados parciales: {num_parciales:,}")
    
    # ========================================================================
    # APLICAR ID MAL ASOCIADO
    # ========================================================================
    num_mal_asociados = int(num_registros * porcentaje_id_mal_asociado / 100)
    if num_mal_asociados > 0:
        print(f"\nAplicando {num_mal_asociados:,} IDs mal asociados...")
        # Asegurarse de no exceder el número de registros disponibles
        indices_disponibles = list(range(min(num_registros, len(filas))))
        indices_mal = random.sample(indices_disponibles, min(num_mal_asociados, len(indices_disponibles)))
        for idx in indices_mal:
            # Mantener ID pero cambiar nombre a otro producto random
            id_correcto = filas[idx][1]
            id_incorrecto = random.choice([i for i in range(1, 101) if i != id_correcto])
            filas[idx][2] = PRODUCTOS[id_incorrecto]  # nombre_producto incorrecto
    
    # ========================================================================
    # APLICAR CAMPOS VACÍOS
    # ========================================================================
    num_vacios = int(num_registros * porcentaje_campos_vacios / 100)
    if num_vacios > 0:
        print(f"Aplicando {num_vacios:,} campos vacíos...")
        # Asegurarse de no exceder el número de registros disponibles
        indices_disponibles = list(range(min(num_registros, len(filas))))
        indices_vacios = random.sample(indices_disponibles, min(num_vacios, len(indices_disponibles)))
        for idx in indices_vacios:
            # Columnas: 2=nombre_producto, 3=precio, 7=ciudad
            columna = random.choice([2, 3, 7])
            filas[idx][columna] = ""
    
    # ========================================================================
    # APLICAR RUIDO (ERRORES DE FORMATO)
    # ========================================================================
    num_ruido = int(num_registros * porcentaje_ruido / 100)
    if num_ruido > 0:
        print(f"Aplicando {num_ruido:,} errores de formato...")
        # Asegurarse de no exceder el número de registros disponibles
        indices_disponibles = list(range(min(num_registros, len(filas))))
        indices_ruido = random.sample(indices_disponibles, min(num_ruido, len(indices_disponibles)))
        for idx in indices_ruido:
            tipo_error = random.choice([
                "ciudad", "precio", "fecha", "id_producto", "id_tienda",
                "nombre_producto", "nombre_tienda"
            ])
            
            if tipo_error == "ciudad" and filas[idx][7]:
                filas[idx][7] = aplicar_ruido_ciudad(filas[idx][7])
            elif tipo_error == "precio" and filas[idx][3]:
                filas[idx][3] = aplicar_ruido_precio(filas[idx][3])
            elif tipo_error == "fecha" and filas[idx][8]:
                try:
                    fecha_obj = datetime.strptime(filas[idx][8], "%Y-%m-%d")
                    filas[idx][8] = aplicar_ruido_fecha(fecha_obj)
                except (ValueError, TypeError):
                    # Si hay error, mantener la fecha original
                    pass
            elif tipo_error == "id_producto":
                filas[idx][1] = aplicar_ruido_id(filas[idx][1])
            elif tipo_error == "id_tienda":
                filas[idx][4] = aplicar_ruido_id(filas[idx][4])
            elif tipo_error == "nombre_producto" and filas[idx][2]:
                opciones = ["upper", "lower", "spaces", "typo"]
                error = random.choice(opciones)
                if error == "upper":
                    filas[idx][2] = filas[idx][2].upper()
                elif error == "lower":
                    filas[idx][2] = filas[idx][2].lower()
                elif error == "spaces":
                    filas[idx][2] = f"  {filas[idx][2]}  "
                else:
                    filas[idx][2] = error_ortografico_simple(filas[idx][2])
            elif tipo_error == "nombre_tienda" and filas[idx][5]:
                opciones = ["upper", "lower", "spaces"]
                error = random.choice(opciones)
                if error == "upper":
                    filas[idx][5] = filas[idx][5].upper()
                elif error == "lower":
                    filas[idx][5] = filas[idx][5].lower()
                else:
                    filas[idx][5] = f" {filas[idx][5]} "
    
    # ========================================================================
    # GUARDAR ARCHIVO CSV
    # ========================================================================
    print(f"\nGuardando archivo {nombre_archivo}...")
    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([
            "id_transaccion", "id_producto", "nombre_producto", "precio",
            "id_tienda", "nombre_tienda", "categoria_tienda", "ciudad", "fecha"
        ])
        writer.writerows(filas)
    
    # ========================================================================
    # RESUMEN FINAL
    # ========================================================================
    print(f"\n{'='*70}")
    print("ARCHIVO GENERADO EXITOSAMENTE")
    print(f"{'='*70}\n")
    print(f"Archivo: {nombre_archivo}")
    print(f"Registros totales generados: {len(filas):,}")
    print(f"Registros base: {num_registros:,}")
    print(f"Registros duplicados añadidos: {registros_duplicados:,}")
    print(f"\nCOLUMNAS GENERADAS:")
    print(f"  - id_transaccion: Identificador único de venta")
    print(f"  - id_producto: ID del producto (1-100)")
    print(f"  - nombre_producto: Nombre del producto")
    print(f"  - precio: Precio de venta en MXN")
    print(f"  - id_tienda: ID de la tienda (1-10)")
    print(f"  - nombre_tienda: Nombre de la tienda")
    print(f"  - categoria_tienda: Premium/Autoservicio/Descuento/Mayoreo/Conveniencia")
    print(f"  - ciudad: CDMX, GDL, MTY, PUEBLA, CANCUN")
    print(f"  - fecha: Fecha de transacción ({fecha_inicio} a {fecha_fin})")
    print(f"\nCALIDAD DE DATOS:")
    print(f"  - Registros duplicados: {registros_duplicados:,} ({porcentaje_duplicados}%)")
    print(f"    - Duplicados exactos: ~{int(registros_duplicados * 0.6):,}")
    print(f"    - Duplicados parciales: ~{int(registros_duplicados * 0.4):,}")
    print(f"  - Registros con IDs mal asociados: {num_mal_asociados:,} ({porcentaje_id_mal_asociado}%)")
    print(f"  - Registros con campos vacíos: {num_vacios:,} ({porcentaje_campos_vacios}%)")
    print(f"  - Registros con errores formato: {num_ruido:,} ({porcentaje_ruido}%)")
    print(f"\nCATÁLOGO DE TIENDAS:")
    for id_t, info in TIENDAS.items():
        print(f"  {id_t}: {info['nombre']} ({info['categoria']})")
    print(f"\n{'='*70}\n")

# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    # Puedes ajustar estos parámetros
    generar_dataset_ventas(
        num_registros=1000000,           # 1 millón de registros
        porcentaje_campos_vacios=5,       # 5% con campos vacíos
        porcentaje_ruido=10,              # 10% con errores de formato
        porcentaje_id_mal_asociado=3,     # 3% con ID-producto mal asociado
        porcentaje_duplicados=3,          # 3% de duplicados (rango 2-4%)
        nombre_archivo="ventas_retail_mexico.csv",
        fecha_inicio="2025-01-01",        # Inicio 2025
        fecha_fin="2025-12-31"            # Fin 2025
    )
