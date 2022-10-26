

/* / { */
/*     keymap { */
/*         compatible = "zmk,keymap"; */

/*         default_layer { */
/*             bindings = < */

/*                &kp W       &kp F       &kp P       &kp B        &kp J       &kp L      &kp U       &kp Y */
/*     &kp A      &kp R       &kp S       &kp T       &kp G        &kp M       &kp N      &kp E       &kp I      &kp O */
/*     &kp Z      &kp X       &kp C       &kp D       &kp V        &kp K       &kp H      &kp COMMA   &kp DOT    &kp SLASH */
/*     &kp Q      &kp N1      &kp N2      &kp N3                               &kp N5     &kp N6      &kp N7     &kp SEMICOLON */

/*                            &kp LSHIFT  &kp LSHIFT                           &kp N1     &kp N2 */
/*                                        &kp LSHIFT                           &kp N3 */
/*                &kp LSHIFT  &kp LSHIFT  &kp LSHIFT                           &kp N4     &kp N5      &mo SYM */

/*             >; */
/*         }; */


/*         SYM { */
/*             bindings = < */

/*                &kp ESC     &kp LBKT    &kp LBRC    &kp B        &kp J       &kp L      &kp U       &kp Y */
/*     &kp A      &kp R       &kp S       &kp T       &kp G        &kp M       &kp N      &kp E       &kp I      &kp O */
/*     &kp Z      &kp X       &kp C       &kp D       &kp V        &kp K       &kp H      &kp COMMA   &kp DOT    &kp SLASH */
/*     &kp Q      &kp N1      &kp N2      &kp N3                               &kp N5     &kp N6      &kp N7     &kp SEMICOLON */

/*                            &kp LSHIFT  &kp LSHIFT                           &kp N1     &kp N2 */
/*                                        &kp LSHIFT                           &kp N3 */
/*                &kp LSHIFT  &kp LSHIFT  &kp LSHIFT                           &kp N4     &kp N5      &kp N6 */

/*             >; */
/*         }; */
/*     }; */
/* }; */



        // zmk,matrix_transform = &default_transform;



//     default_transform: keymap_transform_0 {
//         compatible = "zmk,matrix-transform" ;
//         columns = <12>;
//         rows = <5>;
//            // transform from:
//            // ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
//            // │   │ W │ F │ P │ B │   │   │ J │ L │ U │ Y │   │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
//            // │ A │ R │ S │ T │ G │   │   │ M │ N │ E │ I │ O │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
//            // │ Z │ X │ C │ D │ V │   │   │ K │ H │ , │ . │ / │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
//            // │ Q │ ? │ ? │ ? │   │   │   │   │ ? │ ? │ ? │ ; │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
//            // │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │
//            // └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
//            // transform to:
//            // ┌───┬───┬───┬───┬───┬───┬───┬───┐
//            // │ W │ F │ P │ B │ J │ L │ U │ Y │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┬───┐
//            // │ A │ R │ S │ T │ G │ M │ N │ E │ I │ O │
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
//            // │ Z │ X │ C │ D │ V │ K │ H │ , │ . │ / │
//            // ├───┼───┼───┴───┘
//            // │ Q │ ; │
//            // └───┴───┘
//            //         ┌───┬───┐   ┌───┬───┐
//            //         │ 5 │ 0 │   │11 │ 6 │
//            //         └───┼───┤   ├───┼───┘

//            // to add:
//            // ├───┼───┼───┼───┼───┼───┼───┼───┼───┴───┘
//            // │ Q │ ? │ ? │ ? │ ? │ ? │ ? │ ; │
//            // └───┴───┴───┴───┴───┴───┴───┴───┘

//            // to add:
//            //         ┌───┬───┐   ┌───┬───┐
//            //         │ 2 │ 3 │   │ 8 │ 9 │
//            //         └───┼───┤   ├───┼───┘
//            //             │ 1 │   │10 │
//            //     ┌───┬───┼───┤   ├───┼───┬───┐
//            //     │ 4 │ 5 │ 0 │   │11 │ 6 │ 7 │
//            //     └───┴───┴───┘   └───┴───┴───┘
//                 //         RC(4,2) RC(4,3) RC(4,8) RC(4,9)
//                 //                 RC(4,1) RC(4,10)
//                 // RC(4,4) RC(4,5) RC(4,0) RC(4,11) RC(4,6) RC(4,7)


//         map = <
//         RC(0,1) RC(0,2) RC(0,3) RC(0,4) RC(0,7) RC(0,8) RC(0,9) RC(0,10)
// RC(1,0) RC(1,1) RC(1,2) RC(1,3) RC(1,4) RC(1,7) RC(1,8) RC(1,9) RC(1,10) RC(1,11)
// RC(2,0) RC(2,1) RC(2,2) RC(2,3) RC(2,4) RC(2,7) RC(2,8) RC(2,9) RC(2,10) RC(2,11)
//         RC(3,0) RC(3,1) RC(3,2) RC(3,3) RC(3,8) RC(3,9) RC(3,10) RC(3,11)
//                         RC(4,2) RC(4,3) RC(4,8) RC(4,9)
//                                 RC(4,1) RC(4,10)
//                 RC(4,4) RC(4,5) RC(4,0) RC(4,11) RC(4,6) RC(4,7)
//         >;

//     };

/ {
    keymap {
        compatible = "zmk,keymap";

        default_layer {
            bindings = <
    &kp N1     &kp W      &kp N1     &kp W       &kp F       &kp P       &kp B        &kp J       &kp L      &kp U       &kp Y      &kp N1
    &kp A      &kp R      &kp A      &kp R       &kp S       &kp T       &kp G        &kp M       &kp N      &kp E       &kp I      &kp O
    &kp Z      &kp X      &kp Z      &kp X       &kp C       &kp D       &kp V        &kp K       &kp H      &kp COMMA   &kp DOT    &kp SLASH
    &kp Q      &kp N1     &kp Q      &kp N1      &kp N2      &kp N3      &kp N7       &kp N5     &kp N5     &kp N6      &kp N7     &kp SEMICOLON
    &kp Q      &kp N1     &kp Q      &kp N1      &kp N2      &kp N3      &kp N7       &kp N5     &kp N5     &kp N6      &kp N7     &kp SEMICOLON
            >;
        };
    };
};
