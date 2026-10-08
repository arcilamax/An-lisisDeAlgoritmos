"""Caso real: solicitudes de reserva de aulas de una universidad en un día."""
from modelo import Reserva


def solicitudes_ejemplo():
    return [
        # --- Aula 101 ---
        Reserva("Aula 101", "Monitoría de Cálculo",        8, 10, 120_000),
        Reserva("Aula 101", "Taller de Python",            9, 12, 200_000),
        Reserva("Aula 101", "Curso de extensión",         10, 14, 320_000),
        Reserva("Aula 101", "Tutoría de Física",          12, 14, 150_000),
        Reserva("Aula 101", "Reunión de semillero",       14, 16, 100_000),
        Reserva("Aula 101", "Diplomado de datos",         13, 17, 400_000),
        Reserva("Aula 101", "Capacitación empresarial",   16, 19, 300_000),
        Reserva("Aula 101", "Repaso de Estadística",      17, 19, 170_000),
        Reserva("Aula 101", "Examen de validación",       18, 21, 240_000),
        Reserva("Aula 101", "Club de lectura",            19, 21,  90_000),
        # --- Aula 202 ---
        Reserva("Aula 202", "Sustentación de tesis",       7,  9, 150_000),
        Reserva("Aula 202", "Seminario de IA",             8, 12, 350_000),
        Reserva("Aula 202", "Clase de inglés",             9, 11, 180_000),
        Reserva("Aula 202", "Charla de egresados",        11, 13, 130_000),
        Reserva("Aula 202", "Workshop de UX",             12, 16, 380_000),
        Reserva("Aula 202", "Asesoría de proyectos",      13, 15, 160_000),
        Reserva("Aula 202", "Reunión de profesores",      15, 17, 110_000),
        Reserva("Aula 202", "Taller de liderazgo",        16, 20, 330_000),
        # --- Auditorio ---
        Reserva("Auditorio", "Conferencia de apertura",    8, 11, 500_000),
        Reserva("Auditorio", "Foro de emprendimiento",    10, 13, 450_000),
        Reserva("Auditorio", "Ensayo de grados",          12, 14, 220_000),
        Reserva("Auditorio", "Concierto de la facultad",  14, 18, 600_000),
        Reserva("Auditorio", "Cine foro",                 17, 20, 280_000),
        Reserva("Auditorio", "Conversatorio",             13, 15, 260_000),
    ]
