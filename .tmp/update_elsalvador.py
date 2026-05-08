import os
import re

FILE_PATH = r"c:\Users\12132\Desktop\DigiFacil\DigiFacil\public\el-salvador.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

main_pattern = re.compile(r'<main[^>]*>.*?</main>', re.DOTALL)

new_main_html = """
<main class="pt-24 pb-0 relative overflow-hidden bg-surface">

    <!-- Hero Section -->
    <section class="relative min-h-[85vh] flex flex-col items-center justify-center px-6 md:px-8 mt-12 mb-20 z-10 border-b border-outline-variant/5">
        <div class="absolute inset-0 z-0 bg-primary/5 blur-[120px] rounded-full w-[800px] h-[800px] left-1/2 -translate-x-1/2 pointer-events-none"></div>
        <div class="relative z-10 max-w-5xl text-center">
            
            <span class="inline-block font-label text-primary tracking-[0.2em] mb-6 uppercase text-sm font-bold animate-fade-in border border-primary/20 bg-primary/5 px-6 py-2 rounded-full">Cresca OS El Salvador</span>
            
            <h1 class="font-headline text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold text-white leading-tight tracking-tight mb-8 animate-slide-up">
                Operaciones <span class="text-brand-green italic">Bilingües.</span><br>Ejecución <span class="text-primary italic">Local.</span> Estándares <span class="text-white italic">Globales.</span>
            </h1>
            
            <p class="font-body text-xl md:text-2xl text-on-surface-variant max-w-4xl mx-auto mb-10 leading-relaxed font-light px-4">
                El equipo de Cresca OS en El Salvador es parte fundamental de nuestra operación global.<br><br>
                Desde aquí diseñamos, implementamos y optimizamos sistemas tanto para empresas en Estados Unidos como para negocios locales, bajo los mismos estándares de calidad, estructura y ejecución.<br><br>
                <span class="text-white font-medium">No es un servicio externo. Es parte directa de Cresca OS.</span>
            </p>

            <div class="mt-8 mb-16 relative">
                <a class="signature-texture text-on-primary px-10 py-5 rounded-xl font-label font-bold text-lg shadow-[0_0_30px_rgba(0,230,138,0.3)] transition-all duration-300 hover:scale-105 inline-block uppercase tracking-widest" href="book-audit.html">
                    Agendar Diagnóstico Gratuito
                </a>
            </div>
            
        </div>
    </section>

    <!-- Why El Salvador Segment -->
    <section class="py-32 px-6 md:px-8 bg-surface-container-lowest relative z-10">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
            
            <!-- Context -->
            <div>
                <span class="text-xs font-label tracking-[0.2em] text-brand-green uppercase font-bold mb-4 block">Mismo Estándar. Mejor Ejecución.</span>
                <h2 class="font-headline text-4xl md:text-5xl lg:text-6xl font-bold mb-8 text-white leading-tight">¿Por qué operamos desde El Salvador?</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed mb-6 font-light">
                    Operamos desde El Salvador porque nos permite ofrecer ejecución de alta calidad con velocidad, claridad y consistencia.
                </p>
                <p class="text-on-surface-variant text-xl leading-relaxed mb-10 font-light">
                    Nuestro equipo trabaja en la misma zona horaria que gran parte de Estados Unidos, habla inglés y español con fluidez, y opera bajo los mismos sistemas, procesos y estándares internos.<br><br> <span class="text-brand-green font-medium">Esto se traduce en mejores resultados para nuestros clientes.</span>
                </p>
            </div>
            
            <!-- The Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 relative">
                <div class="absolute inset-0 bg-primary/10 blur-[100px] -z-10 rounded-full"></div>
                
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 shadow-lg hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-primary text-4xl mb-4">schedule</span>
                    <h4 class="font-headline text-2xl font-bold text-white mb-2">Misma Zona Horaria</h4>
                    <p class="text-on-surface-variant text-sm">Soporte rápido, iteraciones directas y sin retrasos operacionales.</p>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 shadow-lg hover:border-brand-green/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-4xl mb-4">language</span>
                    <h4 class="font-headline text-2xl font-bold text-white mb-2">Equipo Bilingüe</h4>
                    <p class="text-on-surface-variant text-sm">Comunicación clara con todo tipo de clientes en su idioma preferido.</p>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 shadow-lg hover:border-primary/30 transition-colors">
                    <span class="material-symbols-outlined text-primary text-4xl mb-4">fact_check</span>
                    <h4 class="font-headline text-2xl font-bold text-white mb-2">Ejecución Consistente</h4>
                    <p class="text-on-surface-variant text-sm">Procesos estructurados y profesionales guiados por metodologías globales.</p>
                </div>
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 shadow-lg hover:border-brand-green/30 transition-colors">
                    <span class="material-symbols-outlined text-brand-green text-4xl mb-4">public</span>
                    <h4 class="font-headline text-2xl font-bold text-white mb-2">Contexto Local</h4>
                    <p class="text-on-surface-variant text-sm">Entendimiento real y profundo del mercado salvadoreño y latino.</p>
                </div>
            </div>
            
        </div>
    </section>

    <!-- Bilingual Advantage & How We Contribute -->
    <section class="py-32 px-6 md:px-8 relative z-10 border-y border-outline-variant/5">
        <div class="max-w-7xl mx-auto space-y-24">
            
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <div class="lg:w-1/2">
                    <span class="text-xs font-label tracking-[0.2em] text-primary uppercase font-bold mb-4 block">La Ventaja Bilingüe</span>
                    <h2 class="font-headline text-4xl md:text-5xl font-bold mb-8 text-white">Comunicación Sin Fricción</h2>
                    <p class="text-on-surface-variant text-lg leading-relaxed mb-6 font-light">
                        Millones de clientes en Estados Unidos prefieren comunicarse en español. Para negocios que atienden este mercado, la comunicación bilingüe ya no es opcional — es una ventaja competitiva.
                    </p>
                    <p class="text-on-surface-variant text-lg leading-relaxed font-light">
                        Cresca OS permite automatizar mensajes, seguimientos y conversaciones en español e inglés de forma natural y consistente, sin fricción.
                    </p>
                </div>
                <div class="lg:w-1/2 relative rounded-3xl overflow-hidden aspect-[4/3] border border-outline-variant/10 shadow-2xl group">
                    <!-- Assuming ops_hub.png or elsalvador_workspace.png exists, using workspace for team representation -->
                    <img src="assets/elsalvador_workspace.png" alt="Cresca OS Team Hub" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-60 mix-blend-luminosity hover:mix-blend-normal">
                    <div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-transparent to-transparent pointer-events-none"></div>
                </div>
            </div>

            <div class="bg-surface-container-low rounded-3xl p-10 md:p-16 border border-outline-variant/10 relative overflow-hidden">
                <div class="absolute -right-32 -top-32 w-96 h-96 bg-brand-green/5 blur-[80px] rounded-full point-events-none"></div>
                <h2 class="font-headline text-3xl md:text-4xl font-bold mb-10 text-white relative z-10 max-w-2xl">Cómo contribuye directamente nuestro equipo en El Salvador:</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-10">
                    <div class="flex gap-4 items-start">
                        <span class="material-symbols-outlined text-brand-green mt-1">settings_suggest</span>
                        <div><strong class="text-white block mb-1">Implementación</strong><p class="text-on-surface-variant text-sm">Configuración profunda de sistemas operativos.</p></div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="material-symbols-outlined text-brand-green mt-1">account_tree</span>
                        <div><strong class="text-white block mb-1">Estructuración CRM</strong><p class="text-on-surface-variant text-sm">Diseño de pipelines y automatizaciones a medida.</p></div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="material-symbols-outlined text-brand-green mt-1">video_camera_front</span>
                        <div><strong class="text-white block mb-1">Onboarding</strong><p class="text-on-surface-variant text-sm">Capacitación en vivo y entrenamiento de clientes.</p></div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="material-symbols-outlined text-brand-green mt-1">monitoring</span>
                        <div><strong class="text-white block mb-1">Monitorización</strong><p class="text-on-surface-variant text-sm">Optimización continua de flujos e infraestructura.</p></div>
                    </div>
                    <div class="flex gap-4 items-start">
                        <span class="material-symbols-outlined text-brand-green mt-1">campaign</span>
                        <div><strong class="text-white block mb-1">Campañas Bilingües</strong><p class="text-on-surface-variant text-sm">Creación e iteración comercial de contenido.</p></div>
                    </div>
                </div>
                <div class="mt-12 pt-8 border-t border-outline-variant/10">
                    <p class="text-lg text-primary font-medium italic">"Esto nos permite ofrecer una ejecución más rápida, soporte más cercano y mayor consistencia en cada proyecto."</p>
                </div>
            </div>

        </div>
    </section>

    <!-- Pricing El Salvador -->
    <section class="py-32 px-6 md:px-8 relative z-10 bg-surface-container-lowest">
        <div class="max-w-7xl mx-auto">
            
            <div class="text-center mb-16 max-w-3xl mx-auto">
                <span class="text-xs font-label tracking-[0.2em] text-brand-green uppercase font-bold mb-4 block">Para negocios en El Salvador</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-6 text-white">Sistemas Accesibles. <br>Resultados Reales.</h2>
                <p class="text-on-surface-variant text-xl leading-relaxed font-light">
                    Hemos diseñado planes adaptados al mercado salvadoreño, con una estructura clara para que puedas empezar, crecer y escalar tu negocio paso a paso.
                </p>
            </div>

            <!-- Tiers Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- Start -->
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex flex-col hover:border-primary/30 transition-colors">
                    <h3 class="font-headline text-2xl font-bold text-white mb-2">Cresca Start</h3>
                    <p class="text-on-surface-variant text-xs mb-6 h-10">Presencia digital, captura de leads y automatización básica.</p>
                    <div class="bg-surface-dim p-4 rounded-xl border border-outline-variant/5 mb-6">
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Setup One-Time</div>
                        <div class="font-headline text-xl text-white mb-4">$0 - $99</div>
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Mensual</div>
                        <div class="font-headline text-3xl text-primary font-bold">$29.99<span class="text-sm text-outline-variant font-normal"> - $49.99</span></div>
                    </div>
                    <div class="mt-auto pt-4 border-t border-outline-variant/10">
                        <p class="text-[11px] text-on-surface-variant">Protección de Datos Integrada disponible por <strong class="text-white">+$29/mes.</strong></p>
                    </div>
                </div>

                <!-- Growth 1 -->
                <div class="bg-surface-container-low p-8 rounded-2xl border border-brand-green/30 flex flex-col hover:border-brand-green/60 transition-colors shadow-lg shadow-brand-green/5 relative overflow-hidden transform lg:-translate-y-2">
                    <div class="absolute top-0 right-0 bg-brand-green text-[#003824] text-[10px] font-bold uppercase tracking-widest py-1 px-3 rounded-bl-lg">Popular</div>
                    <h3 class="font-headline text-2xl font-bold text-white mb-2">Growth 1</h3>
                    <p class="text-on-surface-variant text-xs mb-6 h-10">CRM completo, pipeline y primer flujo de automatización avanzada.</p>
                    <div class="bg-surface-dim p-4 rounded-xl border border-outline-variant/5 mb-6">
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Setup One-Time</div>
                        <div class="font-headline text-xl text-white mb-4">$199 - $299</div>
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Mensual</div>
                        <div class="font-headline text-3xl text-brand-green font-bold">$79<span class="text-sm text-outline-variant font-normal"> - $99</span></div>
                    </div>
                    <div class="mt-auto pt-4 border-t border-outline-variant/10">
                        <p class="text-[11px] text-brand-green">✓ Protección de Datos Integrada incluida.</p>
                    </div>
                </div>

                <!-- Growth 2 -->
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex flex-col hover:border-primary/30 transition-colors">
                    <h3 class="font-headline text-2xl font-bold text-white mb-2">Growth 2</h3>
                    <p class="text-on-surface-variant text-xs mb-6 h-10">Mayor automatización, mejor visibilidad y optimización continua.</p>
                    <div class="bg-surface-dim p-4 rounded-xl border border-outline-variant/5 mb-6">
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Setup One-Time</div>
                        <div class="font-headline text-xl text-white mb-4">$299 - $499</div>
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Mensual</div>
                        <div class="font-headline text-3xl text-primary font-bold">$119<span class="text-sm text-outline-variant font-normal"> - $149</span></div>
                    </div>
                    <div class="mt-auto pt-4 border-t border-outline-variant/10">
                        <p class="text-[11px] text-brand-green">✓ Protección de Datos Integrada incluida.</p>
                    </div>
                </div>

                <!-- Pro Automation -->
                <div class="bg-surface-container p-8 rounded-2xl border border-outline-variant/10 flex flex-col hover:border-primary/30 transition-colors">
                    <h3 class="font-headline text-2xl font-bold text-white mb-2">Pro Auto</h3>
                    <p class="text-on-surface-variant text-xs mb-6 h-10">Sistemas más avanzados para operaciones con mayor complejidad.</p>
                    <div class="bg-surface-dim p-4 rounded-xl border border-outline-variant/5 mb-6">
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Setup One-Time</div>
                        <div class="font-headline text-xl text-white mb-4">Desde $499</div>
                        <div class="font-label text-xs uppercase text-outline-variant font-bold mb-1">Mensual</div>
                        <div class="font-headline text-3xl text-primary font-bold">Desde $199</div>
                    </div>
                    <div class="mt-auto pt-4 border-t border-outline-variant/10">
                        <p class="text-[11px] text-brand-green">✓ Protección de Datos Integrada incluida.</p>
                    </div>
                </div>

            </div>
            
            <div class="mt-8 text-center bg-surface-dim p-4 rounded-xl max-w-4xl mx-auto border border-outline-variant/10">
                <p class="text-xs text-outline font-label uppercase tracking-widest">* El uso de WhatsApp, SMS y correo electrónico se cobra según consumo real, de forma 100% transparente.</p>
            </div>

            <div class="mt-12 text-center">
                <a class="bg-primary hover:bg-primary/90 text-on-primary px-10 py-5 rounded-xl font-label font-bold tracking-widest uppercase transition-all shadow-[0_0_20px_rgba(10,132,255,0.3)] hover:scale-105 inline-block" href="book-audit.html">Agendar Diagnóstico Gratuito</a>
            </div>

        </div>
    </section>

    <!-- Compliance Section -->
    <section class="py-32 px-6 md:px-8 relative z-10 border-y border-outline-variant/5">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-20">
            
            <div>
                <span class="text-xs font-label tracking-[0.2em] text-[#ff8c82] uppercase font-bold mb-6 block">Cumplimiento Institucional</span>
                <h2 class="font-headline text-4xl md:text-5xl font-bold mb-8 text-white">Protege tu negocio y cumple con la ley</h2>
                <p class="text-on-surface-variant text-lg leading-relaxed mb-6 font-light">
                    Las leyes de protección de datos y ciberseguridad ya están vigentes en El Salvador. Si tu negocio maneja información de clientes — nombres, teléfonos, direcciones o reservas — necesitas procesos adecuados para proteger esos datos.
                </p>
                <div class="bg-error-container/20 border border-[#ff8c82]/30 p-6 rounded-xl mb-10">
                    <p class="text-[#ff8c82] font-medium text-sm">Muchos negocios aún operan sin estos controles, lo que los expone a riesgos legales severos y pérdida de confianza financiera.</p>
                </div>
                <p class="text-white text-xl font-bold">Cresca OS integra estos procesos directamente en tu sistema local.</p>
                <div class="mt-12">
                     <a class="bg-surface-container border border-outline-variant/30 text-white hover:bg-surface-variant px-8 py-4 rounded-xl font-label font-bold tracking-widest uppercase shadow-lg transition-all inline-block" href="book-audit.html">Auditoría de Cumplimiento</a>
                </div>
            </div>

            <div class="space-y-10">
                <!-- Lo que exige -->
                <div class="bg-surface-container-low p-8 rounded-2xl border border-outline-variant/10 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-2 h-full bg-[#ff8c82]"></div>
                    <h4 class="font-headline text-2xl font-bold text-white mb-6">Lo que exige la ley:</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-[#ff8c82] text-xl">gavel</span><span class="text-on-surface-variant">Consentimiento claro para el uso de datos.</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-[#ff8c82] text-xl">gavel</span><span class="text-on-surface-variant">Protección estricta contra accesos no autorizados.</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-[#ff8c82] text-xl">gavel</span><span class="text-on-surface-variant">Gestión de solicitudes operativas de clientes.</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-[#ff8c82] text-xl">gavel</span><span class="text-on-surface-variant">Notificación de incidentes en menos de <strong class="text-white">72 horas</strong>.</span></li>
                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-[#ff8c82] text-xl">gavel</span><span class="text-on-surface-variant">Registro inmutable de actividad comercial.</span></li>
                    </ul>
                </div>

                <!-- Como te ayudamos -->
                <div class="bg-surface-container-low p-8 rounded-2xl border border-brand-green/20 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-2 h-full bg-brand-green"></div>
                    <h4 class="font-headline text-2xl font-bold text-brand-green mb-6">Cómo te ayudamos:</h4>
                    <ul class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Flujos de consentimiento</span></li>
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Registro de interacciones</span></li>
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Procesos automáticos</span></li>
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Alertas de seguridad</span></li>
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Privacidad personalizada</span></li>
                        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-brand-green text-sm">check</span><span class="text-on-surface-variant text-sm text-white">Revisión de rendimiento</span></li>
                    </ul>
                </div>

            </div>

        </div>
    </section>

    <!-- Closing Section -->
    <section class="max-w-5xl mx-auto px-6 md:px-8 py-32 text-center relative z-10">
        <div class="bg-primary-container/40 backdrop-blur-md border border-primary/20 p-12 md:p-24 rounded-[2.5rem] shadow-2xl relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-tr from-primary/5 via-transparent to-brand-green/5 mix-blend-overlay pointer-events-none"></div>
            
            <h2 class="font-headline text-4xl md:text-6xl font-bold text-white mb-8 leading-tight relative z-10">Un equipo real. Ejecución real. Resultados reales.</h2>
            <p class="text-on-surface-variant text-xl mb-12 max-w-3xl mx-auto leading-relaxed relative z-10">
                Nuestro equipo en El Salvador es parte directa de Cresca OS. Trabajamos con procesos estructurados, estándares claros y un enfoque implacable en los resultados.<br><br>
                <strong class="text-white">Cuando trabajas con Cresca, sabes exactamente quién está detrás de tu sistema — y cómo se está ejecutando.</strong>
            </p>
            
            <div class="flex flex-col sm:flex-row justify-center items-center gap-6 relative z-10">
                <a href="book-audit.html" class="signature-texture text-on-primary px-10 py-5 rounded-xl font-label font-bold tracking-widest uppercase transition-all shadow-[0_0_20px_rgba(10,132,255,0.3)] hover:scale-105 w-full sm:w-auto">Agendar Diagnóstico Gratuito</a>
                <a class="bg-surface border border-outline-variant/30 text-white hover:bg-surface-variant px-10 py-5 rounded-xl font-label tracking-widest uppercase transition-all w-full sm:w-auto" href="book-audit.html">Hablar con el Equipo</a>
            </div>
            
        </div>
    </section>

</main>
"""

updated_html = re.sub(main_pattern, new_main_html, html)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("El Salvador page has been exquisitely rebuilt.")
