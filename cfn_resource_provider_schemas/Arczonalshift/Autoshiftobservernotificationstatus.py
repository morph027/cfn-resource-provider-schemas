SCHEMA = {
  "typeName" : "AWS::ARCZonalShift::AutoshiftObserverNotificationStatus",
  "description" : "Definition of AWS::ARCZonalShift::AutoshiftObserverNotificationStatus Resource Type",
  "definitions" : {
    "AccountId" : {
      "description" : "User account id, used as part of the primary identifier for the resource",
      "type" : "string",
      "pattern" : "^\\d{12}$"
    },
    "Region" : {
      "description" : "Region, used as part of the primary identifier for the resource",
      "type" : "string",
      "pattern" : "^[a-z0-9-]*$",
      "maxLength" : 30,
      "minLength" : 5
    },
    "AutoshiftObserverNotificationStatus" : {
      "type" : "string",
      "enum" : [ "ENABLED" ]
    }
  },
  "properties" : {
    "Status" : {
      "$ref" : "#/definitions/AutoshiftObserverNotificationStatus"
    },
    "AccountId" : {
      "$ref" : "#/definitions/AccountId"
    },
    "Region" : {
      "$ref" : "#/definitions/Region"
    }
  },
  "readOnlyProperties" : [ "/properties/AccountId", "/properties/Region" ],
  "primaryIdentifier" : [ "/properties/AccountId", "/properties/Region" ],
  "createOnlyProperties" : [ "/properties/Status" ],
  "required" : [ "Status" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "arc-zonal-shift:UpdateAutoshiftObserverNotificationStatus" ]
    },
    "read" : {
      "permissions" : [ "arc-zonal-shift:GetAutoshiftObserverNotificationStatus" ]
    },
    "delete" : {
      "permissions" : [ "arc-zonal-shift:UpdateAutoshiftObserverNotificationStatus", "arc-zonal-shift:GetAutoshiftObserverNotificationStatus" ]
    },
    "list" : {
      "permissions" : [ "arc-zonal-shift:GetAutoshiftObserverNotificationStatus" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  }
}