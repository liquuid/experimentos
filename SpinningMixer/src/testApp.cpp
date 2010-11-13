#include "testApp.h"



//--------------------------------------------------------------
void testApp::setup(){	 
	gears.loadImage("images/disco.gif");
	gears2.loadImage("images/disco.jpg");
	beats.loadSound("sounds/1085.mp3"); 
	beats2.loadSound("sounds/Violet.mp3");
	rpm=rpm2=0 ;
	rpos=rpos2=1 ;
	fftSmoothed = new float[8192];
	for (int i = 0; i < 8192; i++){
		fftSmoothed[i] = 0;
	}

	nBandsToGet = 128;




}


//--------------------------------------------------------------
void testApp::update(){
	ofBackground(255,255,255);	

        float * val = ofSoundGetSpectrum(nBandsToGet);          // request 128 values for fft
        for (int i = 0;i < nBandsToGet; i++){

                // let the smoothed calue sink to zero:
                fftSmoothed[i] *= 0.96f;

                // take the max, either the smoothed or the incoming:
                if (fftSmoothed[i] < val[i]) fftSmoothed[i] = val[i];

        }

}


//--------------------------------------------------------------
void testApp::draw(){
	char tempStr[255];

	ofSetupScreen();
	
	ofSetColor(0xFFFFFF);

	
	glPushMatrix();
	glTranslatef(200,650,150);
	glRotatef(60.0f,1,0,0);
	glRotatef(rpm,0,0,1);

	gears.draw(gears.width/-2,gears.height/-2);
	glPopMatrix();

	
	glPushMatrix();
	glTranslatef(800,650,150);
	glRotatef(60.0f,1,0,0);
	glRotatef(rpm2,0,0,1);

	gears2.draw(gears2.width/-2,gears2.height/-2);
	glPopMatrix();

        ofSetColor(200,200,255,255);
        
        float width = (float)(5*128) / nBandsToGet;
        for (int i = 0;i < nBandsToGet; i++){
                ofRect(100+i*width,200,width,-(fftSmoothed[i] * 200));
        }




	sprintf(tempStr,"rpm = %f rpos = %f rpm2 =%f rpos2 = %f\n",rpm,rpos,rpm2,rpos2);
	ofDrawBitmapString(tempStr, 100 , 300) ;
	rpm+=rpos;
	rpm2+=rpos2;
	if (!beats.getIsPlaying()){
		beats.play();
	}
	if (!beats2.getIsPlaying()){
		beats2.play();
	}

	beats.setSpeed(rpos);
	beats2.setSpeed(rpos2);
}


//--------------------------------------------------------------
void testApp::keyPressed  (int key){ 
	switch(key){
		case OF_KEY_UP:
			if (rpos < 3.0)
				rpos+=0.1;

			break;
		case OF_KEY_DOWN:
			if (rpos > 0.19)
				rpos-=0.1;
			break;
		case OF_KEY_LEFT:
			if (rpos2 < 3.0)
				rpos2+=0.1;

			break;
		case OF_KEY_RIGHT:
			if (rpos2 > 0.19)
				rpos2-=0.1;
			break;
	}
}

//--------------------------------------------------------------
void testApp::keyReleased(int key){ 
	
}

//--------------------------------------------------------------
void testApp::mouseMoved(int x, int y ){
	
}

//--------------------------------------------------------------
void testApp::mouseDragged(int x, int y, int button){
	
}

//--------------------------------------------------------------
void testApp::mousePressed(int x, int y, int button){
	
}

//--------------------------------------------------------------
void testApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::windowResized(int w, int h){

}
