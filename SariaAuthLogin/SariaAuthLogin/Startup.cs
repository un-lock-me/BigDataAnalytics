using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(SariaAuthLogin.Startup))]
namespace SariaAuthLogin
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
