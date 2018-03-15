public abstract class Bee{
	/*
	* the beehive is protected so that the subclasses can access it directly
	*/
	protected BeeHive beeHive

	/*
	* The factory method for creating a bee of a specific role.  It displays a message after creating the new bee:  *BH* {bee} is born 
	* @param rolethe bee's role
	* @param resourcethe bee's resource (only applicable to worker bees)
	* @param beeHivethe bee hive
	* @return the new bee
	*/
	public static Bee createBee(Bee.Role role,                            Worker.Resource resource,                            <a href="../world/BeeHive.html" title="class in world">BeeHive</a> beeHive){ return null; }

	/*
	* Get the bee's role.
	* @return role
	*/
	public Bee.Role getRole(){ return null; }

	/*
	* Return a string representation of the bee in the format:  {ROLE} #{id}  Here, <tt>{ROLE}</tt> is the bee's role, e.g. DRONE, QUEEN or WORKER, and {id} is the unique id of the bee.
	* @return the string described here
	*/
	@Override
	public String toString(){ return  }

	/*
	* Two bees are equal if they have the same id.
	* @param otherthe other thing to compare with
	* @return whether they are equal or not
	*/
	@Override
	public boolean equals(Object other){ return false; }

	/*
	* Since all bee's have unique id's, their hash code is just their id.
	* @return the hash code
	*/
	@Override
	public int hashCode(){ return 0; }

}