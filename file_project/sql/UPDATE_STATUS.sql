-- Update status to Picked
UPDATE hr.files_audit
   SET status = 'PICKED', session_id = <%=odiRef.getSession("SESS_NO")%>, pickup_date = SYSDATE
 WHERE name = '<%=odiRef.getOption("FILENAME")%>'
        
-- Update status to Processed
UPDATE hr.files_audit
   SET status = 'PROCESSED', session_id = <%=odiRef.getSession("SESS_NO")%>, PROCESSED_DATE = SYSDATE
   , load_time_seconds = (SYSDATE - pickup_date)*24*60*60
 WHERE status = 'PICKED'
       AND name = '<%=odiRef.getOption("FILENAME")%>'

-- Update status to Archived
UPDATE hr.files_audit
   SET status = 'ARCHIVED', session_id = <%=odiRef.getSession("SESS_NO")%>
 WHERE status = 'PROCESSED'
       AND name = '<%=odiRef.getOption("FILENAME")%>'       

-- Update status to Error
UPDATE hr.files_audit
   SET status = 'ERROR', session_id = <%=odiRef.getSession("SESS_NO")%>
 WHERE name = '<%=odiRef.getOption("FILENAME")%>'       