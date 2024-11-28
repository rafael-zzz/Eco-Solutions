describe('template spec', () => {
    beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/cadastro/')
    cy.get('#username').type('ong_teste')
    cy.get('#email').type('teste@gmail.com')
    cy.get('#password1').type('ong_teste')
    cy.get('#password2').type('ong_teste')
    cy.get('.bg-green-600').click()

    cy.visit('http://127.0.0.1:8000/admin/')
    cy.get('#id_username').type('admin')
    cy.get('#id_password').type('admin')
    cy.get('.submit-row > input').click()
    })
  
    it('adicionar ong', () => {
        cy.get('.model-ong > :nth-child(2) > .addlink').click();
        cy.get('#id_usuario').select('ong_teste');
        cy.get('.default').click();
        cy.get('.success').should('have.text', 'The ong “ONG” was added successfully.');
      
    })
    afterEach(() => {
        cy.get(':nth-child(1) > .field-__str__ > a').click();
        cy.get('.deletelink').click();
        cy.get('div > [type="submit"]').click();
    })
  })
  