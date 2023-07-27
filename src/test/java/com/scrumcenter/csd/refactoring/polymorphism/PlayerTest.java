package com.scrumcenter.csd.refactoring.polymorphism;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PlayerTest {
    @Test
    public void testWarriorMove() {
        Player warrior = new Player("Warrior");
        assertEquals("Warrior moves forward", warrior.move());
    }

    @Test
    public void testMageMove() {
        Player mage = new Player("Mage");
        assertEquals("Mage teleports", mage.move());
    }

    @Test
    public void testRogueMove() {
        Player rogue = new Player("Rogue");
        assertEquals("Rogue sneaks", rogue.move());
    }
}