describe('template spec', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000/login/');
      cy.get('#username').type('teste_ong');
      cy.get('#password').type('teste_ong');
      cy.get('.bg-green-600').click();
      cy.get(':nth-child(5) > .p-4').click();
      cy.get('#tipo').type('meias');
      cy.get('#quantidade').type('10');
      cy.get('#peso').type('20');
      cy.get('#descricao').type('meia fedorenta');
      cy.get('#addResiduForm > form > .px-4').click();
    });
  
    it('remover residuos', () => {
      cy.get(':nth-child(7) > .p-4').click();
      cy.get('.bg-red-600').click();
      cy.get('#success-message > .bg-green-500').should(($div) => {
        const text = $div.html().replace(/&nbsp;/g, ' ');
        expect(text).to.include('Resíduo removido com sucesso!');
      });
    });
  
    afterEach(() => {
    });
  });
  