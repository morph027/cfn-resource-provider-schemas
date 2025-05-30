SCHEMA = {
  "typeName" : "AWS::Route53::RecordSetGroup",
  "description" : "Resource Type definition for AWS::Route53::RecordSetGroup",
  "additionalProperties" : False,
  "properties" : {
    "Comment" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "HostedZoneName" : {
      "type" : "string"
    },
    "RecordSets" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/RecordSet"
      }
    },
    "HostedZoneId" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "AliasTarget" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DNSName" : {
          "type" : "string"
        },
        "HostedZoneId" : {
          "type" : "string"
        },
        "EvaluateTargetHealth" : {
          "type" : "boolean"
        }
      },
      "required" : [ "HostedZoneId", "DNSName" ]
    },
    "CidrRoutingConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CollectionId" : {
          "type" : "string"
        },
        "LocationName" : {
          "type" : "string"
        }
      },
      "required" : [ "CollectionId", "LocationName" ]
    },
    "GeoProximityLocation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AWSRegion" : {
          "type" : "string"
        },
        "LocalZoneGroup" : {
          "type" : "string"
        },
        "Bias" : {
          "type" : "integer"
        },
        "Coordinates" : {
          "$ref" : "#/definitions/Coordinates"
        }
      }
    },
    "Coordinates" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Longitude" : {
          "type" : "string"
        },
        "Latitude" : {
          "type" : "string"
        }
      },
      "required" : [ "Latitude", "Longitude" ]
    },
    "RecordSet" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HealthCheckId" : {
          "type" : "string"
        },
        "AliasTarget" : {
          "$ref" : "#/definitions/AliasTarget"
        },
        "HostedZoneName" : {
          "type" : "string"
        },
        "ResourceRecords" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "HostedZoneId" : {
          "type" : "string"
        },
        "SetIdentifier" : {
          "type" : "string"
        },
        "TTL" : {
          "type" : "string"
        },
        "Weight" : {
          "type" : "integer"
        },
        "Name" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        },
        "CidrRoutingConfig" : {
          "$ref" : "#/definitions/CidrRoutingConfig"
        },
        "Failover" : {
          "type" : "string"
        },
        "GeoProximityLocation" : {
          "$ref" : "#/definitions/GeoProximityLocation"
        },
        "Region" : {
          "type" : "string"
        },
        "GeoLocation" : {
          "$ref" : "#/definitions/GeoLocation"
        },
        "MultiValueAnswer" : {
          "type" : "boolean"
        }
      },
      "required" : [ "Type", "Name" ]
    },
    "GeoLocation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ContinentCode" : {
          "type" : "string"
        },
        "CountryCode" : {
          "type" : "string"
        },
        "SubdivisionCode" : {
          "type" : "string"
        }
      }
    }
  },
  "createOnlyProperties" : [ "/properties/HostedZoneName", "/properties/HostedZoneId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}