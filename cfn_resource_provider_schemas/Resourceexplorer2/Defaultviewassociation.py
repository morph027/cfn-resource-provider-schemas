SCHEMA = {
  "typeName" : "AWS::ResourceExplorer2::DefaultViewAssociation",
  "description" : "Definition of AWS::ResourceExplorer2::DefaultViewAssociation Resource Type",
  "properties" : {
    "ViewArn" : {
      "type" : "string"
    },
    "AssociatedAwsPrincipal" : {
      "description" : "The AWS principal that the default view is associated with, used as the unique identifier for this resource.",
      "type" : "string",
      "pattern" : "^[0-9]{12}$"
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "ViewArn" ],
  "primaryIdentifier" : [ "/properties/AssociatedAwsPrincipal" ],
  "readOnlyProperties" : [ "/properties/AssociatedAwsPrincipal" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "resource-explorer-2:GetDefaultView", "resource-explorer-2:AssociateDefaultView" ]
    },
    "update" : {
      "permissions" : [ "resource-explorer-2:GetDefaultView", "resource-explorer-2:AssociateDefaultView" ]
    },
    "read" : {
      "permissions" : [ "resource-explorer-2:GetDefaultView" ]
    },
    "delete" : {
      "permissions" : [ "resource-explorer-2:GetDefaultView", "resource-explorer-2:DisassociateDefaultView" ]
    }
  },
  "additionalProperties" : False
}