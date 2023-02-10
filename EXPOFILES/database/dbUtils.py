import psycopg2

def connect():
    return psycopg2.connect(
    host='localhost',
    database='evadb',
    user='evadb',
    password='evadb100'
)


# SELECT
#   (
#     100.0 *
#     COUNT(*)
#     /
#     (
#       SELECT
#         COUNT(*)
#       FROM
#         confirmations
#       WHERE
#         name = 'test'
#         AND
#         created_at >= (current_date - INTERVAL '7 days')
#     )
#   ) AS percentage
# FROM
#   confirmations
# WHERE
#   medname = 'test'
#   AND
#   medicationid = 1
#   AND
#   taken = true
#   AND
#   created_at >= (current_date - INTERVAL '7 days');
