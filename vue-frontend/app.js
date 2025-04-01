const { createApp } = Vue;

createApp({
  data() {
    return {
      termoBusca: "",
      resultados: [],
      carregando: false,
      erro: null,
      timeout: null
    };
  },
  watch: {
    termoBusca(novoTermo) {
      clearTimeout(this.timeout);
      if (novoTermo.length >= 1) {
        // Espera 400ms antes de buscar
        this.timeout = setTimeout(this.buscar, 400);
      } else {
        this.resultados = [];
        this.erro = null;
      }
    }
  },
  methods: {
    selecionar(op) {
        this.termoBusca = op.razao_social;
    },
    async buscar() {
      this.carregando = true;
      this.erro = null;
      try {
        const resposta = await fetch(`http://localhost:8000/busca?q=${this.termoBusca}`);
        console.log("Status da resposta:", resposta.status); // Log do status
        if (!resposta.ok) throw new Error("Erro na requisição: " + resposta.status);
        const dados = await resposta.json();
        console.log("Dados recebidos:", dados); // Adicione este log
        this.resultados = [...dados]; // Força uma nova referência para garantir reatividade
        console.log("Resultados atribuídos:", this.resultados); // Log após atribuição
      } catch (e) {
        this.erro = e.message;
      } finally {
        this.carregando = false;
      }
    }
  }
}).mount("#app");
