import org.springframework.stereotype.Service;
import javax.annotation.PostConstruct;

@Service
public class Fabric {
	@PostConstruct
	public void test() {
		System.out.println("some test method-----------------------------------------------------------------");
	}

}
