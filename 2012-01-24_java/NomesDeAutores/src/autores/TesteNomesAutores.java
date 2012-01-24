package autores;

import junit.framework.TestCase;

public class TesteNomesAutores extends TestCase {
	
	private AuthorNameFormatter authorNameFormatter;
	
	public void setUp(){
		authorNameFormatter = new AuthorNameFormatter();
	}
	
	public void test_um_sobrenome() {		
		assertEquals("SANTOS", authorNameFormatter.format("Santos"));		
	}
	
	public void test_nome_e_sobrenome() {
		assertEquals("SANTOS, Diogo", authorNameFormatter.format("Diogo Santos"));
	}
	
	public void test_nome_e_dois_sobrenomes(){
		assertEquals("MARINS, Raphael Figueiredo", authorNameFormatter.format("Raphael Figueiredo Marins"));
	}
	
}
