using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class UITextScript : MonoBehaviour {
    public Text timeElapsed;
    float totalTime;
    
	// Use this for initialization
	void Start () {
        timeElapsed = GetComponent<Text>();
        totalTime = 0;
	}
	
	// Update is called once per frame
	void Update () {
        totalTime += Time.deltaTime;
        timeElapsed.text = "time elapsed: " + totalTime;
	}

    public void setText(string input)
    {
        timeElapsed.text = input;
    }
}
