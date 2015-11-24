#pragma strict

var speed : float;
private var rb : Rigidbody;

function Start () {
  // http://docs.unity3d.com/ScriptReference/Component-rigidbody.html
  // http://docs.unity3d.com/ScriptReference/GameObject-rigidbody.html
  rb = GetComponent.<Rigidbody>();
  // http://docs.unity3d.com/ScriptReference/Rigidbody.AddForce.html
  rb.AddForce(Vector3.up * 10.0);
}

// Physics
function FixedUpdate () {
  var moveHorizontal : float = Input.GetAxis("Horizontal");
  var moveVertical : float = Input.GetAxis("Vertical");
  
  var movement : Vector3 = new Vector3(moveHorizontal, 0.0, moveVertical);
  
  rb.AddForce(movement * speed);
  /* http://docs.unity3d.com/ScriptReference/Rigidbody-velocity.html
  if (Input.GetButtonDown("Jump")) {
    rb.velocity = Vector3(0,10,0);
  }
  */
  // Vector3 movement = 
}

/*

using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour {

    public float speed;

    private Rigidbody rb;

    void Start ()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate ()
    {
        float moveHorizontal = Input.GetAxis ("Horizontal");
        float moveVertical = Input.GetAxis ("Vertical");

        Vector3 movement = new Vector3 (moveHorizontal, 0.0f, moveVertical);

        rb.AddForce (movement * speed);
    }
}
*/