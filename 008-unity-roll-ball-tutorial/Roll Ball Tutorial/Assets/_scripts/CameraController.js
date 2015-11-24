#pragma strict

var player : GameObject;
private var offset : Vector3;

/*
Tracking does not work in VR
*/

function Start () {
  offset = transform.position - player.transform.position;
}

// CRuns after all other updates
function LateUpdate () {
  transform.position = player.transform.position + offset;
}