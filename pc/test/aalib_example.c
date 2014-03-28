     #include <aalib.h>
     int
     main (int argc, char **argv)
     {
       aa_context *context;       /* The information about currently
                                initialized device.  */
       aa_palette palette;        /* Emulatted palette (optional) */
       aa_savedata sd;
       aa_format format = aa_text_format;
       //format.width =160;
       //format.height =120;

       sd.format = &format;
       //sd.name = "hello.jpg";

       char *framebuffer;

       /* Parse command line options and output the help text.  */
       if (!aa_parseoptions (NULL, NULL, &argc, argv) || argc != 1)
         {
           printf ("%s", aa_help);
           exit (1);
         }

       /* Initialize output driver.  */
       //context = aa_autoinit (&aa_defparams);
       //context = aa_init(&mem_d, &aa_defparams, NULL);
        context = aa_init(&save_d, &aa_defparams, &sd);
       if (context == NULL)
         {
           printf ("Failed to initialize aalib\n");
           exit (1);
         }

       /* Pointer to the emulated videoram.  */
       framebuffer = aa_image (context);


       /* Create palette if needed: */
       //for (i = 0; i < 256; i++)
       //  aa_setpalette (palette, i, /* R value 0..255 */ ,
       //                             /* G value 0..255 */ ,
       //                             /* B value 0..255 */ );

       /* Draw something using: */
       //aa_putpixel (context, /* X coord */ , /* Y coord */ , /* Color */ );

       /* Render whole screen: */
       //aa_renderpalette (context, palette, aa_defrenderparams,
       //             /* Top left conner of rendered area: */ 0, 0,
       //             /* Bottom right */  aa_scrwidth (context), aa_scrheight (context));

       // If you don't use palette use following function:
       aa_render (context, &aa_defrenderparams,
                  0, 0, aa_scrwidth (context), aa_scrheight (context));
       

       /* And make it visible: */
       aa_flush (context);

       /* And uninitialize the AA_lib (this probably makes the picture invisible
          again) */
       aa_close (context);

       return 1;
     }

