from graphviz import Digraph

# Create a new activity diagram specific to Disdukcapil services
disdukcapil_diagram = Digraph("DisdukcapilActivityDiagram", format="png")
disdukcapil_diagram.attr(rankdir="TB", size="8,10")

# Define nodes
disdukcapil_diagram.node("Start", "Mulai", shape="ellipse", style="filled", fillcolor="lightgreen")
disdukcapil_diagram.node("Prep", "Persiapan & Perencanaan\n(Kumpulkan data penduduk, Siapkan infrastruktur)", shape="box", style="rounded, filled", fillcolor="lightblue")
disdukcapil_diagram.node("Dev", "Pengembangan\n(Pemetaan proses layanan KTP, KK, Akta)", shape="box", style="rounded, filled", fillcolor="lightblue")
disdukcapil_diagram.node("Impl", "Implementasi\n(Layanan berbasis SOP, Distribusi informasi)", shape="box", style="rounded, filled", fillcolor="lightblue")
disdukcapil_diagram.node("Eval", "Pemantauan & Evaluasi\n(Tinjau layanan & perbaikan)", shape="box", style="rounded, filled", fillcolor="lightblue")
disdukcapil_diagram.node("End", "Selesai", shape="ellipse", style="filled", fillcolor="lightgreen")

# Define edges
disdukcapil_diagram.edge("Start", "Prep")
disdukcapil_diagram.edge("Prep", "Dev")
disdukcapil_diagram.edge("Dev", "Impl")
disdukcapil_diagram.edge("Impl", "Eval")
disdukcapil_diagram.edge("Eval", "End")

# Render the diagram and save it to a file
disdukcapil_diagram_path = "/mnt/data/disdukcapil_activity_diagram.png"
disdukcapil_diagram.render(disdukcapil_diagram_path, format="png", cleanup=True)

# Return the file path to access the diagram
disdukcapil_diagram_path
