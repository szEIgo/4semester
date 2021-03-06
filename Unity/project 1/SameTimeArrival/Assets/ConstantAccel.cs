﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConstantSpeed1 : MonoBehaviour {
    public float avgSpeed;
    public float totalDistance;
    public bool constantAccel;

    private float speed;
    private float acceleration;
    private float totalTime;
    private float accumulatedTime;
    
    private Rigidbody rigidBody;

    private void Awake()
    {
        rigidBody = GetComponent<Rigidbody>();
        GetComponent<Rigidbody>();
    }

    private void OnEnable()
    {
        

    }

    private void OnDisable()
    {
        
    }

    // Use this for initialization
    private void Start () {
        speed = avgSpeed;
        accumulatedTime = 0;
        calcTime();
        calcAccel();

    }
	
	// Update is called once per frame
	void FixedUpdate () {
        accumulatedTime += Time.deltaTime;
        calcSpeed();
        Move();

        
    }

    private void Move()
    {
        print("speed: " + speed + "; Time.deltatime: " + Time.deltaTime + "; accumulated time: " + accumulatedTime + "; totalTime: " + totalTime);
        // Adjust the position of the tank based on the player's input.
        Vector3 movement = transform.forward * 1 * speed * Time.deltaTime;
        print("transform.forward: " + transform.forward.x + ", " + transform.forward.y + ", " + transform.forward.z);
        print("movement: " + movement.x + ", " + movement.y + ", " + movement.z);
        rigidBody.MovePosition(rigidBody.position + movement);

    }

    private void calcAccel()
    {
        if (constantAccel)
        {
            float halfTime = totalTime / 2;
            float halfDistance = totalDistance / 2;
            float halfWayAverage = halfDistance / halfTime;
            float maxSpeed = halfWayAverage * 2;
            acceleration = maxSpeed / halfTime;
        }
        else
        {
            acceleration = 0;
        }
        
        
    }

    private void calcTime()
    {
        totalTime = totalDistance / avgSpeed;
    }

    private void calcSpeed()
    {

        if (accumulatedTime > totalTime)
        {
            speed = 0;
            return;
        }
        if(accumulatedTime < totalTime / 2)
        {
            speed += acceleration;
        }
        else if (accumulatedTime >= totalTime / 2)
        {
            speed -= acceleration;
        }
        else
        {
            speed = 0;
        }
    }





}
