package autores;

import java.util.Arrays;
import java.util.List;

public class AuthorNameFormatter {

	public String format(String name) {		
		List<String> subNames = Arrays.asList(name.split(" "));
		String lastName = null;
		StringBuilder formattedName = new StringBuilder();
		
		for(String subName : subNames){
			if(lastName != null){				
				formattedName.append(" ").append(lastName);
			}
						
			lastName = firstLetterUp(subName);
		}
		
		lastName = lastName.toUpperCase();
		
		if (formattedName.length() == 0) {
			return lastName;
		} else {
			return lastName + "," + formattedName.toString();
		}
	}
	
	private String firstLetterUp(String word) {
		word = word.toLowerCase();
		word = word.substring(0, 1).toUpperCase() + word.substring(1);
		
		return word;
	}

}
