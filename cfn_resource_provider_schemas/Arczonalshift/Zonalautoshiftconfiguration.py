SCHEMA = {
  "typeName" : "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
  "description" : "Definition of AWS::ARCZonalShift::ZonalAutoshiftConfiguration Resource Type",
  "definitions" : {
    "ZonalAutoshiftStatus" : {
      "type" : "string",
      "enum" : [ "ENABLED" ]
    },
    "ControlCondition" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/ControlConditionType"
        },
        "AlarmIdentifier" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 8,
          "pattern" : "^.*$"
        }
      },
      "required" : [ "AlarmIdentifier", "Type" ],
      "additionalProperties" : False
    },
    "ControlConditionType" : {
      "type" : "string",
      "minLength" : 8,
      "maxLength" : 10,
      "pattern" : "^[a-zA-Z]*$"
    },
    "PracticeRunConfiguration" : {
      "type" : "object",
      "properties" : {
        "BlockingAlarms" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/ControlCondition"
          },
          "maxItems" : 1,
          "minItems" : 1
        },
        "OutcomeAlarms" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/ControlCondition"
          },
          "maxItems" : 1,
          "minItems" : 1
        },
        "BlockedDates" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "maxLength" : 10,
            "minLength" : 10,
            "pattern" : "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
          },
          "maxItems" : 15,
          "minItems" : 0
        },
        "BlockedWindows" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "maxLength" : 19,
            "minLength" : 19,
            "pattern" : "^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}$"
          },
          "maxItems" : 15,
          "minItems" : 0
        }
      },
      "required" : [ "OutcomeAlarms" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ZonalAutoshiftStatus" : {
      "$ref" : "#/definitions/ZonalAutoshiftStatus"
    },
    "PracticeRunConfiguration" : {
      "$ref" : "#/definitions/PracticeRunConfiguration"
    },
    "ResourceIdentifier" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 8
    }
  },
  "createOnlyProperties" : [ "/properties/ResourceIdentifier" ],
  "primaryIdentifier" : [ "/properties/ResourceIdentifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "arc-zonal-shift:CreatePracticeRunConfiguration", "arc-zonal-shift:GetManagedResource", "arc-zonal-shift:UpdateZonalAutoshiftConfiguration", "cloudwatch:DescribeAlarms", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "arc-zonal-shift:GetManagedResource" ]
    },
    "update" : {
      "permissions" : [ "arc-zonal-shift:GetManagedResource", "arc-zonal-shift:UpdatePracticeRunConfiguration", "arc-zonal-shift:UpdateZonalAutoshiftConfiguration", "cloudwatch:DescribeAlarms" ]
    },
    "delete" : {
      "permissions" : [ "arc-zonal-shift:DeletePracticeRunConfiguration", "arc-zonal-shift:GetManagedResource", "arc-zonal-shift:UpdateZonalAutoshiftConfiguration" ]
    },
    "list" : {
      "permissions" : [ "arc-zonal-shift:ListManagedResources" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "allOf" : [ {
    "anyOf" : [ {
      "required" : [ "ZonalAutoshiftStatus" ]
    }, {
      "required" : [ "PracticeRunConfiguration" ]
    } ],
    "allOf" : [ {
      "required" : [ "ResourceIdentifier" ]
    } ]
  } ]
}