const form = document.getElementById("predictionForm");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        "Disaster Type": document.getElementById("disasterType").value,
        "Start Year": parseInt(document.getElementById("startYear").value),
        "Total Deaths": parseFloat(document.getElementById("totalDeaths").value),
        "No. Injured": parseFloat(document.getElementById("noInjured").value),
        "Total Affected": parseFloat(document.getElementById("totalAffected").value),
        "Total Damage ('000 US$)": parseFloat(document.getElementById("totalDamage").value),
        "Magnitude": parseFloat(document.getElementById("magnitude").value),
        "Country": document.getElementById("country").value
    };

    try {
        const response = await fetch("http://localhost:5000/prever", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            resultado.innerHTML = `<strong>Nível de Risco:</strong> ${result["Nivel de Risco"]}`;
        } else {
            resultado.innerHTML = `<span style="color:red;">Erro: ${result.error}</span>`;
        }

    } catch (error) {
        resultado.innerHTML = `<span style="color:red;">Erro ao conectar com o servidor.</span>`;
    }
});