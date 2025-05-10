


async function calcular() {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;
    const operacion = document.getElementById("operacion").value;

    const url = `/${operacion}?a=${a}&b=${b}`;
    try {
        const res = await fetch(url);
        const data = await res.json();

        if (res.ok) {
            document.getElementById("resultado").textContent = `Resultado: ${data.resultado}`;
        } else {
            document.getElementById("resultado").textContent = `Error: ${data.detail}`;
        }
    } catch (error) {
        document.getElementById("resultado").textContent = "Error al conectar con el servidor.";
    }
}
