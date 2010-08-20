/***************************************************************************

This source file is part of OGREBULLET
(Object-oriented Graphics Rendering Engine Bullet Wrapper)
For the latest info, see http://www.ogre3d.org/phpBB2addons/viewforum.php?f=10

Copyright (c) 2007 tuan.kuranes@gmail.com (Use it Freely, even Statically, but have to contribute any changes)



This source file is not LGPL, it's public source code that you can reuse.
-----------------------------------------------------------------------------*/

#include "OgreBulletListener.h"
#include "OgreBulletInputListener.h"

using namespace Ogre;
using namespace OIS;


// -------------------------------------------------------------------------
OgreBulletInputListener::OgreBulletInputListener(OgreBulletListener * ogreBulletListener,
                                                 Ogre::RenderWindow *win) :

    mButton0Pressed (false),
    mButton1Pressed (false),
    mButton2Pressed  (false),
    mWindow (win),
    mListener(ogreBulletListener)
{
    mMouseCursorX = 0.5;
    mMouseCursorY = 0.5;

}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseClicked(BULLET_MOUSE_EVENT e)
{
    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseEntered(BULLET_MOUSE_EVENT e)
{
    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseExited(BULLET_MOUSE_EVENT e)
{
    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mousePressed(BULLET_MOUSE_EVENT e , OIS::MouseButtonID buttonid)
{
    if (BULLET_BUTTON0_DOWN)
    {
        mButton0Pressed = true;
        mListener->button0Pressed();
    }
    else if (BULLET_BUTTON1_DOWN)
    {
        mButton1Pressed = true;
        mListener->button1Pressed();
    }
    else if (BULLET_BUTTON2_DOWN)
    {
        mButton2Pressed = true;
        mListener->button2Pressed();
    }


    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseReleased(BULLET_MOUSE_EVENT e, OIS::MouseButtonID buttonid)
{

    if (BULLET_BUTTON0_UP)
    {
        mButton0Pressed = false;
        mListener->button0Released ();
    }
    if (BULLET_BUTTON1_UP)
    {
        mButton1Pressed = false;
        mListener->button1Released ();
    }
    if (BULLET_BUTTON2_UP)
    {
        mButton2Pressed = false;
        mListener->button2Released ();
    }


    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseDragged(BULLET_MOUSE_EVENT e)
{
    // This populates the cursor moves or camera rotation variables
    mRelX = BULLET_GETRELX;
    mRelY = BULLET_GETRELY;

    mMouseCursorX = Real(BULLET_GETX) / mWindow->getWidth ();
    mMouseCursorY = Real(BULLET_GETY) / mWindow->getHeight ();

    mListener->mouseMoved ();


    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::mouseMoved(BULLET_MOUSE_EVENT e)
{
    // This populates the cursor moves or camera rotation variables
    mRelX = BULLET_GETRELX;
    mRelY = BULLET_GETRELY;

    mMouseCursorX = Real(BULLET_GETX) / mWindow->getWidth ();
    mMouseCursorY = Real(BULLET_GETY) / mWindow->getHeight ();


    mListener->mouseMoved ();

    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::keyClicked(BULLET_KEY_EVENT e)
{
    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::keyPressed(BULLET_KEY_EVENT e)
{
    mListener->keyPressed(BULLET_GETKEY);
    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}
// -------------------------------------------------------------------------
BULLET_LISTENER_IMPLEMENTATION_RETURN OgreBulletInputListener::keyReleased(BULLET_KEY_EVENT e)
{
    mListener->keyReleased(BULLET_GETKEY);


    BULLET_LISTENER_IMPLEMENTATION_RETURN_CODE
}