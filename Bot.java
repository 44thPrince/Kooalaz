import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import javax.security.auth.login.LoginException;

public class Bot extends ListenerAdapter {
    private JDA jda;

    public Bot() throws LoginException, InterruptedException {
        jda = JDABuilder.createDefault(
                /* bot token */)
                .addEventListeners(this)
                .build(); //creates the connection to discord and brings the bot online
        jda.awaitReady(); //starts the waiting loop
    }

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        /*
            This is where all of the bot's code goes, if it gets annoyingly long some of the code could
            be moved to other methods or even classes

            Functions mainly through conditionals
        */
        User author = event.getAuthor();
        Message msg = event.getMessage();
        MessageChannel channel = event.getChannel();

        if(msg.getContentRaw().equalsIgnoreCase("+ping")) {
            long time = System.currentTimeMillis();
            channel.sendMessage("pong!").queue(response -> {
                response.editMessageFormat("Pong: %d ms", System.currentTimeMillis() - time).queue();
            });
        }

        else if(msg.getContentRaw().equalsIgnoreCase("+msg")) { //msg.getContentRaw() returns the text of a message
            channel.sendMessage("message") //self-explanatory
                    .queue(); //this needs to be added at the end of every bot action so that the bot actually does it
            msg.delete().queue(); //the message with the prefix in it gets deleted
        }

        else if(msg.getContentRaw().equalsIgnoreCase("+attendance")) {

        }

        else if(msg.getContentRaw().equalsIgnoreCase("+setup user")) {

        }

        else if(msg.getContentRaw().equalsIgnoreCase("+help")) {

        }

        else if(msg.getContentRaw().equalsIgnoreCase("+setup server")) {

        }

        else if(msg.getContentRaw().equalsIgnoreCase("+start")) {

        }

    }

}
