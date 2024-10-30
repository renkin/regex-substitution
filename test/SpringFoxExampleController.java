package com.example;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

/**
 * An example controller
 */
@RestController
@RequestMapping("/internal/entity")
public class InternalEntityController {

    private final InternalEntityService internalEntityService;


    @Autowired
    public InternalEntityController(InternalEntityService internalEntityService) {
        this.internalEntityService = internalEntityService;
    }

    @PostMapping("/{id}/setVariables")
    @ApiOperation("Set a variable at the internal entity")
    @ApiResponses({
            @ApiResponse(code = 200, message = "Variable replacment started successfully."),
    })
    public void setVariable(
            @ApiParam(value = "The entity id", required = true) @PathVariable("entityId") String entityId,
            @Valid @ApiParam(value = "Variable values to be set", required = true) @RequestBody VariableValueDO variableValues) {
        internalEntityService.setVariable(id, variableValues);
    }
}
