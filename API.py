import requests

headers = {"ET-Client-Name": "DITTKLIENTNAVN-HER"}


def run_query(query):
    request = requests.post('https://api.entur.io/journey-planner/v3/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Feilkode {}. {}".format(request.status_code, query))


query = """

{
  stopPlace(id: "NSR:StopPlace:XXXX") {
    id
    name
    estimatedCalls(timeRange: 72100, numberOfDepartures: 10) {
      realtime
      aimedDepartureTime
      expectedDepartureTime
      destinationDisplay {
        frontText
      }
      quay {
        id
      }
      serviceJourney {
        journeyPattern {
          line {
            id
	    publicCode
            name
          }
        }
      }
    }
  }
}
"""


result = run_query(query)


def getProps (estimatedCall):
    return {
	'linje': estimatedCall['serviceJourney']['journeyPattern']['line']['publicCode'],
        'destinasjon': estimatedCall['destinationDisplay']['frontText'],
        'sanntid': estimatedCall['expectedDepartureTime']
        
    }


filteredDataList = []
for estimatedCall in result['data']['stopPlace']['estimatedCalls']:
   filteredDataList.append(getProps(estimatedCall))


print(filteredDataList)

