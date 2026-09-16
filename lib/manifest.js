/* NUTRICYT — datos editables del sitio.
   Cambia aquí el número de WhatsApp y los enlaces de Cal.com sin tocar el resto del código. */
(function () {
  "use strict";

  window.__NUTRICYT__ = {
    whatsappNumber: "18097499916",

    // Mensaje genérico usado por el widget de chat flotante.
    whatsappGenericMessage: "Hola, quiero información sobre tus consultas de nutrición",

    // EDITA AQUÍ: correo donde quieres recibir los mensajes del formulario de contacto.
    contactEmail: "contacto@nutricyt.com",

    // EDITA AQUÍ: enlaces de Cal.com por servicio (cada uno con su propia duración).
    calLinks: {
      evaluacionInicial: "[CAL_LINK_EVALUACION_INICIAL]",
      asesoriaPersonal: "[CAL_LINK_ASESORIA_PERSONAL]",
      estiloVida: "[CAL_LINK_ESTILO_VIDA]",
      seguimiento: "[CAL_LINK_SEGUIMIENTO]",
      evaluacionDeportiva: "[CAL_LINK_EVALUACION_DEPORTIVA]",
    },
  };
})();
