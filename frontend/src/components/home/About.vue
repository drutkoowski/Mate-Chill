<template>
  <h1 class="text-center">O nas</h1>
  <div class="wrapper">
    <div class="about__container">
      <p>
        &emsp;Jesteśmy zespołem z pasją do Yerba Mate. Naszym celem jest
        dostarczanie najwyższej jakości produktów z Ameryki Południowej i
        umożliwienie naszym klientom cieszenia się autentycznym doświadczeniem z
        picia tej popularnej herbaty. <br />
        <br />Nasza oferta zawiera szeroką gamę produktów, w tym różne rodzaje
        popularnej Yerbki, bombille, kalabasse i akcesoria niezbędne do
        delektowania się tym zacnym trunkiem w tradycyjny sposób. Wszystkie
        nasze produkty pochodzą od zaufanych dostawców i są starannie wybierane,
        aby zapewnić najlepszą jakość i smak.
      </p>
      <p>
        &emsp;Stawiamy na umożliwienie naszym klientom poznawania i cieszenia
        się naszymi produktami w sposób, który jest autentyczny, smaczny i
        dostępny dla wszystkich. <br /><br />Dlatego zawsze staramy się być
        dostępni do Waszej dyspozycji i odpowiadać na wszystkie pytania
        dotyczące naszych produktów i ich użycia. <br />Serdecznie zapraszamy do
        skorzystania z naszej oferty!
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
};
</script>

<style scoped lang="scss">
h1,
p {
  color: var(--primary-white);
}
h1 {
  font-size: 3rem;
  margin-top: 5rem;
  @include respond(tab-sm) {
    font-size: 2rem;
  }
}
.wrapper {
  display: grid;
  grid-template-columns: 0.15fr 1fr 0.15fr;
  margin-top: 5rem;
  @include respond(md-desktop) {
    grid-template-columns: 1fr;
  }
  .about__container {
    grid-column: 2/3;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-column-gap: 5rem;
    @include respond(md-desktop) {
      grid-column: 1/2;
    }
    @include respond(tab-sm) {
      font-size: 1rem;
      grid-template-columns: 1fr;
      grid-row-gap: 3rem;
    }
    @include respond(phone-md-lg) {
      font-size: 0.8rem;
    }
  }
}
</style>
