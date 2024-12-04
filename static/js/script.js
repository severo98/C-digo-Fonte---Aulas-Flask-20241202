function validarSenha() {
  const senha = document.getElementById('senha').value;
  const senhaRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{6,}$/;
  
  if (!senhaRegex.test(senha)) {
      alert('A senha deve ter no mínimo 6 caracteres, uma letra maiúscula, um número e um caractere especial.');
      return false;
  }
  return true;
}

function validarCadastro() {
  const senha = document.getElementById('senha').value;
  const confirmacao_senha = document.getElementById('confirmacao_senha').value;
  
  if (senha !== confirmacao_senha) {
      alert('As senhas não coincidem!');
      return false;
  }
  return true;
}
